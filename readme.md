# AI-Powered Early Disease Detection

## Overview
This AI-powered system analyzes medical images (X-rays, MRIs, and dermoscopic images) to detect early-stage diseases, including **Pneumonia, Bone Fractures, and Skin Cancer**. The goal is to assist doctors in quick diagnosis, reduce their workload, and provide timely treatment, especially in underprivileged communities with limited access to healthcare.

## Features
- **Pneumonia Detection**: Identifies signs of pneumonia in chest X-ray images.
- **Bone Fracture Detection**: Detects fractures in X-ray images and highlights the affected area.
- **Skin Cancer Classification**: Classifies skin lesions into six categories:
  - **Actinic Keratosis** (Pre-cancerous skin patch)
  - **Basal Cell Carcinoma** (Common skin cancer)
  - **Benign Keratosis-like Lesion** (Harmless skin spot)
  - **Dermatofibroma** (Small, firm skin bump)
  - **Melanoma** (Dangerous skin cancer)
  - **Melanocytic Nevus** (Normal mole or birthmark)
- **User-friendly Web Interface**: Built using **Streamlit** for easy accessibility.
- **Works on Low-Cost Hardware**: Optimized for deployment in resource-limited settings.
- **Sustainable Healthcare Solution**: Reduces the need for excessive medical tests, saving time and resources.

## Technologies Used
- **Python**
- **Deep Learning (PyTorch, TensorFlow)**
- **Transformers for Image Processing**
- **Streamlit** (for Web UI)
- **OpenCV & PIL** (for image preprocessing)

## Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Create a virtual environment & install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload a medical image (X-ray, MRI, or skin lesion photo).
2. Select the disease detection option.
3. Click **"Analyze"** to get instant predictions.
4. View the results, including detected disease and confidence scores.

## Contributors  
- [Charchil Raj](https://www.linkedin.com/in/charchilraj)  
- [Suryansh Rai](https://www.linkedin.com/in/suryanshrai011)  



## Contact
For questions or suggestions, feel free to reach out or create an issue on GitHub.

---
🚀 **Empowering early disease detection through AI!**

