# 📦 Amazon Delivery Time Prediction

An end-to-end Machine Learning project that predicts Amazon delivery duration using operational, environmental, and delivery-related factors. The solution combines data preprocessing, feature engineering, model development, evaluation, and deployment through an interactive Streamlit application.


## 🚀 Project Overview

Timely delivery is a critical factor in customer satisfaction and logistics efficiency. Delivery duration is influenced by several variables, including distance, weather conditions, traffic congestion, vehicle type, and delivery agent characteristics.

This project leverages Machine Learning to estimate delivery time based on these factors, enabling data-driven decision-making in logistics operations.

---

## 🎯 Objective

Develop a predictive model capable of accurately estimating delivery time using historical delivery data and deploy the solution through a user-friendly web application.

---

## 📊 Features Used

### Numerical Features
- Delivery Distance (km)
- Agent Age
- Agent Rating
- Order Hour
- Order Weekday

### Categorical Features
- Weather Conditions
- Traffic Level
- Vehicle Type
- Delivery Area
- Product Category

### Engineered Features
- Weekend Indicator
- Time-Based Features
- One-Hot Encoded Variables

---

## 🔬 Machine Learning Workflow

### 1. Data Preprocessing
- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Categorical Encoding

### 2. Exploratory Data Analysis (EDA)
- Distribution Analysis
- Feature Relationships
- Delivery Pattern Analysis
- Correlation Assessment

### 3. Model Development
Multiple regression models were evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### 4. Model Selection
The **Gradient Boosting Regressor** achieved the best overall performance and was selected for deployment.

---

## 📈 Model Performance

| Metric | Score |
|----------|----------|
| MAE | 30.5 |
| RMSE | 41.1 |
| R² Score | 0.37 |

### Best Performing Model
✅ Gradient Boosting Regressor

---

## 🛠️ Tech Stack

### Programming
- Python

### Data Science Libraries
- Pandas
- NumPy
- Scikit-learn

### Deployment
- Streamlit

### Model Serialization
- Pickle

### Development Tools
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 📂 Project Structure

```text
amazon-delivery-time-prediction/
│
├── app.py
├── best_delivery_model.pkl
├── requirements.txt
├── Amazon_DeliveryTime_Analysis.ipynb
└── README.md
```

---

## 💻 Application Features

- Interactive Streamlit Interface
- Real-Time Delivery Time Prediction
- Automated Feature Processing
- Dynamic User Inputs
- Machine Learning-Powered Predictions

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/amazon-delivery-time-prediction.git
```

### Navigate to Project Directory

```bash
cd amazon-delivery-time-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```


## 🌐 Deployment

The project is deployed using **Streamlit Community Cloud**, allowing users to interact with the model through a web-based interface.

**Live Demo:** _Add Deployment Link Here_

---

## 📌 Key Skills Demonstrated

- Data Cleaning & Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning Model Development
- Model Evaluation & Selection
- Model Deployment
- Python Programming
- Streamlit Development

---

## 🚀 Future Enhancements

- Hyperparameter Optimization
- Real-Time Weather API Integration
- Traffic API Integration
- Geospatial Feature Engineering
- Ensemble Learning Approaches
- MLOps Pipeline Implementation
- Cloud-Based Model Monitoring

---

## 📖 Conclusion

This project demonstrates an end-to-end Machine Learning workflow for solving a real-world logistics problem. By transforming raw delivery data into actionable insights, the model provides a practical approach to delivery time estimation and showcases the application of predictive analytics in supply chain operations.

---

## 👨‍💻 Author

**Himanshu**
