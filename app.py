import streamlit as st
from module import predict_image
import os

# Set Streamlit page configuration
st.set_page_config(
    page_title="Medi Assist - Pneumonia Detection",
    page_icon="🩺",
    layout="wide"
)

# ---- TOP BAR ----
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

# ---- SIDEBAR ----
st.sidebar.header("About This App")
st.sidebar.write("This AI-powered tool detects **Pneumonia** from chest X-ray images using Deep Learning.")

st.sidebar.header("How to Use")
st.sidebar.write("""
1. Upload a **chest X-ray image** 📤  
2. Wait for the **AI model to analyze** 🧠  
3. Get a **prediction along with confidence score** 🏥  
""")

# ---- MAIN UI ----
st.title("🩺 Medi Assist - Pneumonia Detection")

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
        # Predict the result
        label, confidence = predict_image(file_path)

        # Show the result
        st.markdown("#### 🔍 Prediction Result")
        st.success(f"**{label}**")
        st.write(f"**Confidence Score:** {confidence:.2f}")

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
