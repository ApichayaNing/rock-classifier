import gdown
import os
import tensorflow as tf
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

model_path = 'rock_classifier_model.keras'
google_drive_file_id = '1pDC-f7gY8_o-frRZ3A_oIsO4cmYxwg2t'

# Check if model already downloaded
if not os.path.exists(model_path):
    url = f'https://drive.google.com/uc?id={google_drive_file_id}'
    st.write("Downloading model from Google Drive...")
    gdown.download(url, model_path, quiet=False)

# Load the model
model = tf.keras.models.load_model(model_path)

class_names = ['Basalt', 'Marble', 'Granite', 'Slate', 'Sandstone']

st.title("Rock Classifier - Multiple Images")

uploaded_files = st.file_uploader("Upload one or more rock images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    cols = st.columns(2)  # Display in 2 columns
    for idx, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file).convert('RGB')
        
        # Preprocess
        img_resized = img.resize((224, 224))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        preds = model.predict(img_array)
        pred_label = class_names[np.argmax(preds)]
        
        # Display
        with cols[idx % 2]:
            st.image(img, caption=f"Prediction: {pred_label}", use_column_width=True)
