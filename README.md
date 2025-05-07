# 🪨 Rock Classifier (Deep Learning)

Hey there! 👋 Welcome to my very first machine learning project:  
A deep learning image classifier trained to identify 5 types of rocks:

👉 **basalt, granite, marble, sandstone, slate**

I built this using TensorFlow + MobileNetV2 + a *lot* of Google Colab hours. 😅

## 🤓 Quick summary:

- **Training accuracy:** reached ~85%  
- **Validation accuracy:** hovered ~50-60%  
- **Fine-tuned 30 extra epochs:** validation stayed stable, no overfitting
- Currently makes the best guesses it can—but hey, it’s rocks, and they’re tricky!

I’m **super proud of the results so far**, but definitely planning to keep improving this project with more data, better augmentation, and more experimentation!

👉 Feel free to try it out LIVE here:  
🎉 **[Try the Rock Classifier App](https://rock-classifier-awa5pxsxepza7ukdyybiur.streamlit.app)**

Let me know if it calls your marble a granite 🤭

---

## 💻 Features

✅ Transfer learning with MobileNetV2  
✅ Fine-tuning with class weights  
✅ Works with single or multiple uploaded images  
✅ Predicts your rock and gives a confidence score  
✅ Deployed via Streamlit Cloud → easy to use in your browser

---

## 📊 Example predictions

**First test → initial training (40 epochs) + fine-tuning (10 epochs):**

![example](https://github.com/user-attachments/assets/be61fb47-b351-4c09-a5be-484948c00a73)

The model was tested on 8 **unseen images** (not part of training data).

✅ Correct predictions:  
- 1st (granite)  
- 3rd (basalt)  
- 6th (slate)

❌ Incorrect predictions:  
- 2nd (should be marble)  
- 4th, 5th, 7th, 8th (all misclassified as granite)

Result: **3/8 correct predictions on unseen test data.**

➡️ It’s learning! Still struggles with visually similar rocks, but that’s the adventure.

---

## 🚀 How to use

1. Open the app [here](https://rock-classifier-awa5pxsxepza7ukdyybiur.streamlit.app)
2. Upload one or more rock images
3. See what the model thinks your rock is 🪨
4. Wonder whether geology is harder than coding 😄

---

## 📝 Notes

⚠️ This is a prototype trained on a small dataset. Accuracy will improve as I continue adding data and experimenting.

💬 Got feedback? Let me know → I’d love to learn and make this better!

---

## 📚 Technologies

- TensorFlow
- Keras
- Streamlit
- Google Colab
- Python

---

## 🙌 Thanks for checking it out!

I made this project to learn more about machine learning and image classification, and honestly—it’s been so fun! I’m excited to keep iterating, adding more samples, and seeing how good it can get.

👉 Try it → break it → send me cool rock pics 😄
