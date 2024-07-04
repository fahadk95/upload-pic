import streamlit as st
from PIL import Image

# Start the Camera
with st.expander("Upload image"):
    uploaded_image = st.file_uploader("Upload Image")
print(uploaded_image)

# Create a Pillow image
if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)
