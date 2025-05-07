# 🪨 Rock Classifier (Deep Learning)

A deep learning image classifier built with TensorFlow + MobileNetV2 to classify 5 types of rocks: **basalt, granite, marble, sandstone, slate.**

## 💻 Features
- Transfer learning using MobileNetV2
- Fine-tuning with class weights
- Achieved ~75% training accuracy and ~50-60% validation accuracy on small dataset
- Predicts from uploaded image (with Streamlit interface)

## 📊 Example 1st training with 40epoch / fine-10epoch
![example](https://github.com/user-attachments/assets/be61fb47-b351-4c09-a5be-484948c00a73)
This image shows 8 test rock samples with their predicted labels from the model.

✅ The model correctly predicted **3 out of 8** samples:
- Correct predictions: granite (top-left), marble (top-center), basalt (top-right).
- Incorrect predictions: misclassified other samples (e.g., sandstone and slate predicted as granite).

This result shows the model performs well on some rock types but struggles to differentiate similar textures or colors, especially for granite vs. sandstone. Further improvement is needed to increase accuracy across all classes.


## 🚀 How to use
1. Upload an image of a rock
2. The model will predict the type
3. Shows confidence score

## 📝 Notes
⚠️ Prototype trained on small dataset; accuracy can be improved with more data and tuning.

## 📚 Technologies
- TensorFlow
- Keras
- Streamlit
- Python
- Google Colab
