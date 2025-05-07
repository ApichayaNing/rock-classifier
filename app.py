import gdown
import os
import tensorflow as tf

model_path = 'rock_classifier_model.keras'
google_drive_file_id = '1pDC-f7gY8_o-frRZ3A_oIsO4cmYxwg2t'


if not os.path.exists(model_path):
    url = f'https://drive.google.com/uc?id={google_drive_file_id}'
    print("Downloading model from Google Drive...")
    gdown.download(url, model_path, quiet=False)

# Load the model
model = tf.keras.models.load_model(model_path)

import streamlit as st
from PIL import Image
import numpy as np

st.title("Rock Classifier")

uploaded_file = st.file_uploader("Upload a rock image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict
    preds = model.predict(img_array)
    class_names = ['Basalt', 'Marble', 'Granite', 'Slate', 'Sandstone']
    pred_label = class_names[np.argmax(preds)]
    
    st.write(f"**Prediction:** {pred_label}")
