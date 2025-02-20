import os
import cv2
import numpy as np
import zipfile
import io
import tempfile
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
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

skin_cancer_detector_path = os.path.join("Model","model.zip")

# def load_skin_model_from_zip(zip_path):
#     with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#         with tempfile.TemporaryDirectory() as temp_dir:
#             zip_ref.extractall(temp_dir)  # Extract to a temporary directory

#             # Find the model file inside extracted files
#             model_path = os.path.join(temp_dir, "model.h5")  # Change this if needed

#             # Load the model
#             model = tf.keras.models.load_model(model_path)
    
#     return model

# def process_skin_image(image_path, target_size=(224, 224)):
#     """
#     Processes an image for model prediction.

#     Parameters:
#         image_path (str): Path to the image file.
#         target_size (tuple): Desired image size (default: (224, 224)).

#     Returns:
#         numpy.ndarray: Preprocessed image array.
#     """
#     img = load_img(image_path, target_size=target_size)
#     img_array = img_to_array(img) / 255.0
#     img_array = np.expand_dims(img_array, axis=0)
#     return img_array

# def predict_skin_image(image_path):
#     """
#     Loads the model from zip, processes the image, and returns predictions.

#     Parameters:
#         model_zip_path (str): Path to the zipped model file.
#         image_path (str): Path to the image file for prediction.

#     Returns:
#         numpy.ndarray: Prediction output from the model.
#     """
#     model = load_skin_model_from_zip(skin_cancer_detector_path)
#     img_array = process_skin_image(image_path)
#     benign_prob, malignant_prob = model.predict(img_array)[0]
#     return benign_prob,malignant_prob



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
