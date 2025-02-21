import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image


# Get absolute path to the model
model_path = os.path.join("Model", "Medical_Assistant.h5")

# Debugging: Print the absolute model path
print("Loading model from:", model_path)

# Check if the model file exists before loading
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

# Load the saved model
model = load_model(model_path)

# Function to preprocess the image
def preprocess_pneumonia_image(image_path):
    img_size = 150  # Model input size
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    img = cv2.resize(img, (img_size, img_size))  # Resize to 150x150
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to make prediction
def predict_pneumonia_image(image_path):
    processed_img = preprocess_pneumonia_image(image_path)
    prediction = model.predict(processed_img)[0][0]  # Get prediction score
    label = "PNEUMONIA" if prediction > 0.5 else "NORMAL"
    return label, prediction

# Function for which will unzip the skin cancer detector model and process the image for the 
# Load Skin Cancer Classifier Model
skin_processor = AutoImageProcessor.from_pretrained("NeuronZero/SkinCancerClassifier")
skin_model = AutoModelForImageClassification.from_pretrained("NeuronZero/SkinCancerClassifier")

def skin_cancer_prediction(skin_image_path):
    skin_image = Image.open(skin_image_path).convert("RGB")

    # Preprocess image
    skin_inputs = skin_processor(images=skin_image, return_tensors="pt")

    # Perform inference
    with torch.no_grad():
        skin_outputs = skin_model(**skin_inputs)

    # Get predicted class
    skin_logits = skin_outputs.logits
    skin_predicted_class = skin_logits.argmax(-1).item()

    # Get class labels
    # skin_id2label = skin_model.config.id2label
    skin_id2label = {
        5: "Melanocytic Nevus (Benign Mole)",  # NV
        4: "Melanoma (Skin Cancer)",  # MEL
        0: "Actinic Keratosis (Precancerous Lesion)",  # AK
        1: "Basal Cell Carcinoma (Skin Cancer)",  # BCC
        3: "Dermatofibroma (Non-Cancerous Skin Growth)",  # DF
        2: "Benign Keratosis-like Lesion (Harmless Skin Spot)"  # BKL
    }
    skin_prediction_label = skin_id2label[skin_predicted_class]
    return skin_prediction_label

# this is for the Bone fracture classification

fracture_processor = AutoImageProcessor.from_pretrained("Heem2/bone-fracture-detection-using-xray")
fracture_model = AutoModelForImageClassification.from_pretrained("Heem2/bone-fracture-detection-using-xray")

def classify_fracture(image_path):
    # Load image
    image = Image.open(image_path).convert("RGB")  # Ensure RGB mode

    # Preprocess the image
    inputs = fracture_processor(images=image, return_tensors="pt")  # Convert to PyTorch tensor

    # Perform inference
    with torch.no_grad():
        outputs = fracture_model(**inputs)

    # Get predicted class
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=-1).item()

    # Mapping the class index to a label
    class_labels = fracture_model.config.id2label  # Hugging Face model label mapping

    return class_labels[predicted_class]  # Return the predicted label
