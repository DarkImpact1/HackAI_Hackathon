import streamlit as st
from module import predict_image
import os

if __name__ == "__main__":
    st.set_page_config(page_title="Medi Assist - Pneumonia Detection", page_icon="🩺", layout="centered")

        
    # Streamlit UI
    st.title("🩺 Medi Assist - Pneumonia Detection")

    # File uploader
    uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        # Save uploaded file
        file_path = os.path.join("sample_images", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the uploaded image
        st.image(file_path, caption="Uploaded Image", use_container_width=True)

        # Predict the result
        label, confidence = predict_image(file_path)

        # Show the result
        st.write(f"### Prediction: **{label}**")
        st.write(f"Confidence Score: {confidence:.2f}")
