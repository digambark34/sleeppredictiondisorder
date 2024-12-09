# Sleep Disorder Prediction System

A machine learning-powered web application to predict sleep disorders based on health and lifestyle inputs. This project uses **Random Forest** and **Support Vector Machine (SVM)** models, with SVM deployed on **Streamlit** for real-time predictions.

---

## 📋 Project Overview
The **Sleep Disorder Prediction System** is designed to assist users in identifying the likelihood of sleep disorders based on their input data. The system leverages a health and lifestyle dataset to train machine learning models for accurate predictions. It is user-friendly, easy to access, and can be deployed on both local and cloud environments.

---

## 🧠 Features
- Predicts the likelihood of a sleep disorder based on health metrics.
- Interactive web interface built with **Streamlit**.
- User-friendly input forms for real-time predictions.
- Backend powered by a trained **Support Vector Machine (SVM)** model saved as a `.pkl` file.
- Deployed model for efficient prediction and easy integration.

---

## 🗂️ Dataset
The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset), containing the following features:
- **Person ID**: Unique identifier for individuals.
- **Gender, Age, Occupation**: Basic demographics.
- **Sleep Duration, Sleep Quality**: Indicators of sleep behavior.
- **Physical Activity Level, Stress Level**: Lifestyle-related metrics.
- **BMI Category, Heart Rate, Blood Pressure**: Health-related data.
- **Daily Steps**: Activity data.
- **Sleep Disorder**: Target label (Yes/No).

---

## 🔍 Machine Learning Models
### 1. **Random Forest Classifier**
- An ensemble method that uses decision trees for classification.
- Tested for accuracy, recall, and precision.

### 2. **Support Vector Machine (SVM)**
- A supervised learning algorithm optimized using an RBF kernel.
- Deployed using the `pickle` module to save the trained model as `sleep_disorder_model.pkl`.

---

## 🚀 Deployment
The model is deployed on **Streamlit**. Users can input their health and lifestyle details through an interactive web interface, and the SVM model predicts whether the user might have a sleep disorder.

---

## 🛠️ Installation and Usage

### Prerequisites
- Python 3.7 or above.
- Required libraries listed in the `requirements.txt` file.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sajidkassari/Sleep-Disorder-Prediction.git
   cd sleep-disorder-prediction
   
2. ## Install Dependencies:
   ```bash
   pip install -r requirements.txt

3. Run Streamlit file
   ```bash
    streamlit run main.py
   
4. Access at Localhost
   ```bash
    http://localhost:8501



