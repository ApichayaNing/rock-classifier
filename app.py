import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model('model/trained_model.h5')

# Class names
class_names = ['basalt', 'granite', 'marble', 'sandstone', 'slate']

st.title("🪨 Rock Classifier")
st.write("Upload a rock image and I'll predict the type!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        # Preprocess
        img_resized = img.resize((224, 224))
        img_array = image.img_to_array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_label = class_names[predicted_index]
        confidence = prediction[0][predicted_index]

        st.write(f"### Prediction: {predicted_label}")
        st.write(f"Confidence: {confidence:.2f}")
