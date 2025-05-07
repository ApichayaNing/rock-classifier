# 🪨 Rock Classifier (Deep Learning)

A deep learning image classifier built with TensorFlow + MobileNetV2 to classify 5 types of rocks: **basalt, granite, marble, sandstone, slate.**

## 💻 Features
- Transfer learning using MobileNetV2
- Fine-tuning with class weights
- Achieved ~75% training accuracy and ~50-60% validation accuracy on small dataset
- Predicts from uploaded image (with Streamlit interface)

## 📊 Example 1st training with 40epoch / fine-10epoch
![example](https://github.com/user-attachments/assets/be61fb47-b351-4c09-a5be-484948c00a73)
This image shows the first test of the rock classifier using **unseen images (not part of training data)** after the initial training (40 epochs) and fine-tuning (10 epochs).

✅ The model correctly predicted **3 out of 8 images**:
- Correct predictions: 1st (granite), 3rd (basalt), 6th (slate).
- Incorrect predictions: 2nd (should be marble), 4th, 5th, 7th, and 8th (misclassified as granite).

Result: **3/8 correct predictions on unseen test data.**

➡️ This shows the model has learned some rock features but still struggles with similar textures (e.g., granite vs sandstone or marble). Further improvements can be made with more training data, tuning, and augmentation.


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
