import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

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
def preprocess_image(image_path):
    img_size = 150  # Model input size
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Read as grayscale
    img = cv2.resize(img, (img_size, img_size))  # Resize to 150x150
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=-1)  # Add channel dimension
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to make prediction
def predict_image(image_path):
    processed_img = preprocess_image(image_path)
    prediction = model.predict(processed_img)[0][0]  # Get prediction score
    label = "PNEUMONIA" if prediction > 0.5 else "NORMAL"
    return label, prediction
