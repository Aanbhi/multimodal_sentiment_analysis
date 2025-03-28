import streamlit as st
import requests
from PIL import Image
import io

# Backend API endpoint (replace with actual URL when deployed)
API_URL_TEXT = "https://b2b0-34-16-200-36.ngrok-free.app/text_sentiment"
API_URL_IMAGE = "https://b2b0-34-16-200-36.ngrok-free.app/image_sentiment"

# Streamlit UI Setup
st.set_page_config(page_title="Multimodal Sentiment Analysis", layout="wide")
st.title("Multimodal Sentiment Intelligence Platform")

# Sidebar for input selection
st.sidebar.header("User Input")
input_type = st.sidebar.radio("Select Input Type", ("Text", "Image"))

if input_type == "Text":
    st.subheader("Text Sentiment Analysis")
    user_text = st.text_area("Enter text below")
    
    if st.button("Analyze Sentiment"):
        if user_text.strip():
            response = requests.post(API_URL_TEXT, json={"text": user_text})
            if response.status_code == 200:
                sentiment_result = response.json()
                st.write("Sentiment Result:", sentiment_result['sentiment'])
            else:
                st.error("An error occurred while processing your request. Please try again.")
        else:
            st.warning("Input text cannot be empty.")

elif input_type == "Image":
    st.subheader("Image Sentiment Analysis")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Analyze Sentiment"):
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            img_bytes = img_bytes.getvalue()
            
            response = requests.post(API_URL_IMAGE, files={"file": img_bytes})
            if response.status_code == 200:
                sentiment_result = response.json()
                st.write("Sentiment Result:", sentiment_result['sentiment'])
            else:
                st.error("An error occurred while processing your request. Please try again.")

# Footer
st.markdown("---")
st.markdown("Developed by Anbhi Thakur | [GitHub Repository](https://github.com/Aanbhi/multimodal_sentiment_analysis)")
