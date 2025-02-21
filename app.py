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
    st.title("🩺 Medi Assist")
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
    st.header("How to Use")
    st.write("""
             1. Select the disease you want to detect from the dropdown menu.
             2. Upload a chest X-ray image.
             3. Wait for the AI model to analyze.
             4. Get a prediction along with confidence score.
             5. Repeat for more images or try different models.
            """)
    # ---- SIDEBAR ----
    st.sidebar.header("About This App")
    st.sidebar.write("""
                     ### **AI-Powered Early Disease Detection System**  

This is an AI model capable of analyzing medical images (X-rays, MRIs, etc.) to detect early-stage diseases such as cancer, tuberculosis, and fractures with high accuracy.
                      This technology aims to assist doctors by providing rapid and reliable diagnostics, reducing their workload and enabling faster treatment decisions.
                     By leveraging AI for early detection, the system can significantly improve patient outcomes while ensuring accessibility for underprivileged
                     communities through compatibility with low-cost hardware. Additionally, this solution promotes sustainability by minimizing
                     the need for excessive medical tests, optimizing resource utilization, and enhancing healthcare efficiency.
                     """)


def main_ui():

    # ---- MAIN UI ----
    
        # Dropdown for disease selection
    # option = st.selectbox("Select Disease to Detect:", ["Detect Pneumonia", "Detect Fracture","Detect Skin Cancer"])
    option = st.radio("Select Disease to Detect:", ["Detect Pneumonia", "Detect Fracture", "Detect Skin Cancer"])

    # File uploader
    uploaded_file = st.file_uploader("Upload a Chest X-ray Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        # Create a directory if not exists
        os.makedirs("sample_images", exist_ok=True)
        
        # Save uploaded file
        file_path = os.path.join("sample_images", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the uploaded image with proper alignment
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(file_path, caption="🖼 Uploaded Image", use_container_width=True)

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
        # Remove the uploaded image
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