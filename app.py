import streamlit as st
import os
from module import predict_pneumonia_image, classify_fracture, skin_cancer_prediction


# Set Streamlit page configuration
def configure_page():
    st.set_page_config(
        page_title="Medi Assist - AI Diagnosis",
        page_icon="🩺",
        layout="wide"
    )


# ---- TOP BAR ----
def top_bar():
    st.markdown(
        """
        <style>
            .top-bar {
                background-color: #0a66c2;
                color: white;
                padding: 10px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                border-radius: 5px;
            }
            .top-bar a {
                color: white;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
        <div class="top-bar">
            Developed by 
            <a href="https://www.linkedin.com/in/mohit-dwivedi13" target="_blank">Mohit Dwivedi</a> 🩺
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("🩺 Medi Assist - AI Diagnosis")

    st.write("""
    ### **AI-Powered Early Disease Detection System**  

    **Medi Assist** is an **AI-driven virtual assistant for doctors**, helping them **save time** by providing rapid and reliable diagnostic insights.  
    It can detect **pneumonia, fractures, and skin cancer** from medical images with high accuracy.

    ### **Key Benefits:**  
    ✅ **Early Detection:** AI-powered analysis for timely medical intervention.  
    ✅ **Time-Saving:** Automates image analysis, reducing doctors’ workload.  
    ✅ **Accessible Healthcare:** Works on low-cost devices, benefiting underprivileged communities.  
    ✅ **Sustainability:** Optimizes resources, reducing unnecessary tests.  
    """)

    st.sidebar.header("How to Use")
    st.sidebar.write("""
        1. Select the disease to detect.
        2. Upload an image or capture one using your camera.
        3. AI will analyze and provide a **diagnosis** with a **confidence score**.
    """)


# ---- MAIN UI ----
def main_ui():
    # Disease Selection
    st.write("### Select Disease to Detect:")
    option = st.radio("", ["Detect Pneumonia", "Detect Fracture", "Detect Skin Cancer"])

    # Image Upload or Camera Input
    st.write("### Upload an Image or Capture Using Camera:")
    upload_option = st.radio("", ["Upload an Image", "Upload Using Camera"])

    uploaded_file = None
    captured_image = None

    if upload_option == "Upload an Image":
        uploaded_file = st.file_uploader("Upload an X-ray Image:", type=["jpg", "png", "jpeg"])
    elif upload_option == "Upload Using Camera":
        captured_image = st.camera_input("Capture an Image Using Camera",label_visibility="hidden")
    else:
        st.error("Please select How would you like to upload medical image")

    # Process Image
    if uploaded_file or captured_image:
        image_source = uploaded_file if uploaded_file else captured_image

        # Save Image
        os.makedirs("sample_images", exist_ok=True)
        file_path = os.path.join("sample_images", "captured_image.jpg")

        with open(file_path, "wb") as f:
            f.write(image_source.getbuffer())

        # Display Image
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(file_path, caption="🖼 Uploaded/Captured Image", use_container_width=True)

        with col2:
            st.markdown("#### 🔍 Prediction Result")
            if option == "Detect Pneumonia":
                label, confidence = predict_pneumonia_image(file_path)
                st.success(f"**{label}**")
                st.write(f"**Confidence Score:** {confidence:.2f}")

            elif option == "Detect Fracture":
                fracture_prediction = classify_fracture(image_path=file_path)
                st.success(f"**{fracture_prediction}**")

            elif option == "Detect Skin Cancer":
                skin_prediction = skin_cancer_prediction(skin_image_path=file_path)
                st.success(f"**{skin_prediction}**")

        # Remove Image After Processing
        os.remove(file_path)

    # ---- FOOTER ----
    st.markdown("---")
    st.markdown(
        """
        <p style="text-align:center;">
            Developed by <a href="https://www.linkedin.com/in/mohit-dwivedi13" target="_blank">Mohit Dwivedi</a>,
            <a href="https://www.linkedin.com/in/charchilraj" target="_blank">Charchil Raj</a>, and 
            <a href="https://www.linkedin.com/in/suryanshrai011" target="_blank">Suryansh Rai</a> | 
            © 2025 Medi Assist
        </p>
        """,
        unsafe_allow_html=True
    )


# ---- MAIN FUNCTION ----
def main():
    configure_page()
    top_bar()
    main_ui()


if __name__ == "__main__":
    main()