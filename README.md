# Customer Churn Prediction Web App

An end-to-end Machine Learning project that predicts whether a customer is likely to churn, using a trained ML pipeline and a Flask-based web application.

---

## 📌 Project Overview

Customer churn refers to customers leaving a service or subscription.  
This project builds a **classification model** to predict churn based on customer demographics, services, and billing information, and deploys it as a simple web application.

---

## 🚀 Features

- End-to-end ML pipeline using **Scikit-learn**
- Data preprocessing with:
  - Imputation
  - PowerTransformer
  - OneHotEncoding
- Binary classification for churn prediction
- Flask web application for user interaction
- Displays **churn prediction and churn probability**
- Clean UI using HTML & CSS
- Fully version-controlled using GitHub

---

## 🧠 Machine Learning Details

- **Problem Type:** Binary Classification  
- **Target Variable:** Churn (Yes / No)
- **Model Used:** Decision Tree Classifier
- **Evaluation Focus:** Recall for churn customers

### Preprocessing Pipeline
- **Numeric features:** Missing value imputation + PowerTransformer  
- **Categorical features:** Missing value imputation + OneHotEncoder  
- **Binary features:** Yes/No mapped to 0/1  
- Entire preprocessing and model saved as a single pipeline (`pipeline.pkl`)

---

## 📁 Project Structure

churn-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│ └── pipeline.pkl
│
├── notebooks/
│ └── churn_model_training.ipynb
│
├── data/
│ └── telco_churn.csv
│
├── templates/
│ └── index.html
│
└── static/
└── style.css


---

## 🖥️ How to Run Locally

## 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd churn-app

##2️⃣ Install dependencies

pip install -r requirements.txt

##3️⃣ Run the Flask application

python app.py

##4️⃣ Open in browser
