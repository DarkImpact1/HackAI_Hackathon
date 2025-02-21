import streamlit as st
from module import predict_pneumonia_image, classify_fracture, skin_cancer_prediction
import os

# Set Streamlit page configuration
def configure_page():
    st.set_page_config(
        page_title="Medi Assist - Pneumonia Detection",
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
            Developed by <a href="https://www.linkedin.com/in/mohit-dwivedi13" target="_blank">Mohit Dwivedi</a> 🩺
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("🩺 Medi Assist")

    # ---- SIDEBAR ----
    st.write("""
    ### **AI-Powered Early Disease Detection System**  

    Medi Assist is an AI-driven diagnostic assistant designed to analyze medical images (X-rays, MRIs, etc.) and detect early-stage diseases such as cancer, tuberculosis, and fractures with high accuracy.  

    This project serves as a **virtual assistant for doctors**, helping them **save time** by providing rapid and reliable diagnostic insights. By automating the initial analysis of medical images, it reduces the workload of healthcare professionals, allowing them to focus on **treating more patients** efficiently.  

    ### **Key Benefits:**  
    ✅ **Early Detection:** AI-powered analysis enables the identification of diseases at an early stage, leading to timely medical intervention.  
    ✅ **Time-Saving for Doctors:** Automates image analysis, reducing manual workload and speeding up decision-making.  
    ✅ **Accessible Healthcare:** Designed to work on low-cost hardware, ensuring medical assistance reaches underprivileged communities.  
    ✅ **Sustainability:** Optimizes medical resources by minimizing unnecessary tests, improving healthcare efficiency.  

    By leveraging AI for early disease detection, this system enhances patient outcomes, supports doctors in managing more cases, and contributes to a **scalable and efficient healthcare ecosystem**.  
    """)

    st.sidebar.header("How to Use")
    st.sidebar.write("""
             1. Select the disease you want to detect from the dropdown menu.
             2. Choose to upload an image or capture one using your camera.
             3. Wait for the AI model to analyze.
             4. Get a prediction along with confidence score.
             5. Repeat for more images or try different models.
            """)


def main_ui():

    # ---- MAIN UI ----
    
        # radio button for disease selection
    st.write("### Select Disease to Detect:")
    option = st.radio("", ["Detect Pneumonia", "Detect Fracture", "Detect Skin Cancer"])

    # File uploader or Camera Input
    st.write("### Upload an Image or Capture Using Camera:")
    file_uploade_opt = st.radio("## choose how would you like to upload the image", ["Upload an Image", "Capture Image Using Camera"])
    uploaded_file = None
    captured_image = None
    if file_uploade_opt == "Upload an Image":
        uploaded_file = st.file_uploader("Upload an X-ray Image:", type=["jpg", "png", "jpeg"])
    else:
        captured_image = st.camera_input("Or Capture Image Using Camera")
    # uploaded_file = st.file_uploader("Upload an X-ray Image:", type=["jpg", "png", "jpeg"])
    # captured_image = st.camera_input("Or Capture Image Using Camera")

    if uploaded_file or captured_image:
        # Determine the file source
        image_source = uploaded_file if uploaded_file else captured_image

        # Create a directory if not exists
        os.makedirs("sample_images", exist_ok=True)

        # Save uploaded/captured file
        file_path = os.path.join("sample_images", "captured_image.jpg")
        with open(file_path, "wb") as f:
            f.write(image_source.getbuffer())

        # Display the uploaded/captured image
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(file_path, caption="🖼 Uploaded/Captured Image", use_container_width=True)

        with col2:
            # Perform prediction based on selection
            st.markdown("#### 🔍 Prediction Result")
            if option == "Detect Pneumonia":
                label, confidence = predict_pneumonia_image(file_path)
                st.success(f"**{label}**")
                st.write(f"**Confidence Score:** {confidence:.2f}")

            elif option == "Detect Fracture":
                fracture_prediction = classify_fracture(image_path=file_path)
                st.write(f"**{fracture_prediction}**")

            elif option == "Detect Skin Cancer":
                skin_prediction = skin_cancer_prediction(skin_image_path=file_path)
                st.write(f"**{skin_prediction}**")

        # Remove the image file after processing
        os.remove(file_path)



    # ---- FOOTER ----
    st.markdown("---")
    st.markdown(
        """
        <p style="text-align:center;">
            Developed by  <a href="https://www.linkedin.com/in/mohit-dwivedi13" target="_blank">Mohit Dwivedi</a>
            ,<a href="https://www.linkedin.com/in/charchilraj" target="_blank">Charchil Raj</a> and 
            <a href="https://www.linkedin.com/in/suryanshrai011" target="_blank">Suryansh Rai</a> | 
            © 2025 Medi Assist
        </p>
        """,
        unsafe_allow_html=True
    )
    
    
    
    
def main():
    configure_page()
    top_bar()
    main_ui()
    
    
    
if __name__ == "__main__":
    main()