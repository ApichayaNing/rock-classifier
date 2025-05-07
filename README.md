# 🪨 Rock Classifier (Deep Learning)

A deep learning image classifier built with TensorFlow + MobileNetV2 to classify 5 types of rocks: **basalt, granite, marble, sandstone, slate.**

## 💻 Features
- Transfer learning using MobileNetV2
- Fine-tuning with class weights
- Achieved ~75% training accuracy and ~50-60% validation accuracy on small dataset
- Predicts from uploaded image (with Streamlit interface)

## 📊 Example
![example](https://github.com/user-attachments/assets/be61fb47-b351-4c09-a5be-484948c00a73)
This image shows 8 rock samples tested with the model. The predicted class is shown above each image.

✅ The model correctly predicted **6 out of 8** samples:
- Correctly classified granite, marble, basalt, and slate.
- Misclassified the reddish sandstone as granite (due to similar texture/color).
- Correctly identified the white granite.

This highlights the model’s strengths in recognizing granite and slate, while also showing that similar colors or textures (like sandstone and granite) can cause misclassification.

Overall, the model achieved **75% accuracy on this test set**.


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
