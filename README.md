# 📦 Amazon Delivery Time Prediction

An end-to-end Machine Learning project that predicts **Amazon delivery time** using operational, environmental, geographical, and delivery-related factors.

The project covers the complete Machine Learning lifecycle — from **data cleaning and feature engineering to EDA, model training, MLflow experiment tracking, model evaluation, and Streamlit deployment**.

---

## 🚀 Project Overview

Delivery time is affected by multiple real-world factors such as:

* Delivery distance
* Traffic conditions
* Weather conditions
* Vehicle type
* Delivery area
* Product category
* Delivery agent age
* Agent rating
* Order time
* Day of the week

This project uses historical delivery data to build a regression model that estimates the expected delivery duration for a new order.

The final model is deployed through an interactive **Streamlit web application** where users can enter delivery details and receive an estimated delivery time.

---

## 🎯 Objectives

* Clean and preprocess raw delivery data
* Handle missing values and duplicate records
* Perform Exploratory Data Analysis (EDA)
* Calculate delivery distance using the **Haversine Formula**
* Create time-based features
* Encode categorical variables using One-Hot Encoding
* Train and compare multiple regression models
* Track experiments and metrics using **MLflow**
* Select the best-performing model using test-set RMSE
* Save the trained model for deployment
* Build an interactive Streamlit prediction application

---

## 💼 Business Motivation

Accurate delivery-time prediction can help logistics operations:

* Improve customer satisfaction
* Provide better delivery-time estimates
* Optimize delivery resources
* Understand the impact of traffic and weather
* Evaluate delivery-agent performance
* Support data-driven logistics decisions

---

## 📊 Features Used

### Numerical Features

* Agent Age
* Agent Rating
* Delivery Distance (km)
* Order Hour
* Order Weekday
* Weekend Indicator

### Categorical Features

* Weather Condition
* Traffic Level
* Vehicle Type
* Delivery Area
* Product Category

### Engineered Features

#### 📍 Haversine Distance

The distance between the store and customer delivery location is calculated using latitude and longitude coordinates with the Haversine formula.

```text
Store Coordinates
       ↓
Customer Coordinates
       ↓
Haversine Formula
       ↓
Distance_km
```

#### 🕒 Time-Based Features

The project extracts:

* Order Hour
* Order Weekday
* Is Weekend

These features help the model capture time-related delivery patterns.

#### 🔢 One-Hot Encoding

Categorical variables such as weather, traffic, vehicle, area, and product category are converted into numerical features using One-Hot Encoding.

---

## 🔬 Machine Learning Workflow

```text
Raw Delivery Data
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Duplicate Removal
        ↓
Feature Engineering
        ↓
Haversine Distance Calculation
        ↓
Time-Based Features
        ↓
One-Hot Encoding
        ↓
Exploratory Data Analysis
        ↓
Train-Test Split
        ↓
Model Training
        ↓
MLflow Experiment Tracking
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Model Serialization
        ↓
Streamlit Deployment
```

---

## 🧹 Data Preprocessing

The preprocessing pipeline includes:

* Removing duplicate records
* Cleaning whitespace from categorical columns
* Handling textual `"NaN"` values
* Filling missing categorical values
* Filling missing agent ratings using the mean
* One-hot encoding categorical features
* Removing unnecessary date/time columns before modeling
* Removing raw GPS coordinates after extracting useful distance information
* Handling remaining missing values using `SimpleImputer`

The model training pipeline uses a Scikit-learn `Pipeline`, ensuring preprocessing and model inference remain consistent.

---

## 📈 Exploratory Data Analysis

The project performs EDA to understand the relationship between delivery time and different factors.

### Visualizations include:

* Delivery Time Distribution
* Delivery Distance Distribution
* Delivery Time Boxplot
* Agent Rating Distribution
* Orders by Day of Week
* Traffic vs Delivery Time
* Weather vs Delivery Time
* Vehicle Type vs Delivery Time
* Delivery Area vs Delivery Time
* Distance vs Delivery Time
* Agent Rating vs Delivery Time
* Numerical Correlation Heatmap
* Agent Performance Analysis

---

## 🤖 Machine Learning Models

Three regression models were trained and compared:

### 1. Linear Regression

Used as a baseline regression model.

### 2. Random Forest Regressor

An ensemble learning algorithm capable of capturing nonlinear relationships and feature interactions.

### 3. Gradient Boosting Regressor

A boosting-based ensemble method that builds multiple weak learners sequentially to improve prediction performance.

All models are implemented inside Scikit-learn pipelines with a `SimpleImputer` for consistent missing-value handling.

---

## 🏆 Model Selection

The models were evaluated using:

* **MAE — Mean Absolute Error**
* **RMSE — Root Mean Squared Error**
* **R² Score**
* **Cross-Validation RMSE**

The final model is selected based on the **lowest test-set RMSE**.

### Best Performing Model

**Random Forest Regressor** 🌲

### Test Set Performance

| Metric   |  Score |
| -------- | -----: |
| MAE      | ≈ 17.3 |
| RMSE     | ≈ 22.5 |
| R² Score | ≈ 0.81 |

These metrics indicate that the final model explains a substantial portion of the variation in delivery time while maintaining a relatively low prediction error.

---

## 📊 MLflow Experiment Tracking

MLflow is used to track the model training experiments.

For each model, the project records:

* Model parameters
* MAE
* RMSE
* R² Score
* Cross-Validation RMSE
* Model artifacts where supported

The experiment is organized under:

```text
Amazon_Delivery_Time_Prediction
```

This makes it easier to compare different models and reproduce the training process.

---

## 💾 Model Serialization

After model comparison, the best-performing pipeline is saved using Pickle:

```text
best_delivery_model.pkl
```

The saved pipeline contains the trained model and preprocessing logic required during prediction.

The Streamlit application loads this saved model and uses it to generate predictions.

---

## 🌐 Streamlit Application

The project includes an interactive Streamlit application.

Users can enter:

* Distance
* Agent Age
* Agent Rating
* Order Date
* Order Time
* Weather Condition
* Traffic Level
* Vehicle Type
* Delivery Area
* Product Category

The application then performs the required feature engineering and generates an estimated delivery time.

### Prediction Flow

```text
User Input
    ↓
Feature Engineering
    ↓
Categorical Encoding
    ↓
Feature Alignment
    ↓
Trained Random Forest Pipeline
    ↓
Predicted Delivery Time
```

The application displays the final prediction in minutes.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Experiment Tracking

* MLflow

### Deployment

* Streamlit

### Model Serialization

* Pickle

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📂 Project Structure

```text
amazon-delivery-time-prediction/
│
├── app.py
├── best_delivery_model.pkl
├── cleaned_amazon_delivery.csv
├── model_results.csv
├── requirements.txt
├── Amazon_DeliveryTime_Analysis.ipynb
└── README.md
```

> `cleaned_amazon_delivery.csv` and `model_results.csv` are generated during the notebook workflow. Include them in the repository only if you want to make the processed dataset and model comparison results available.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/amazon-delivery-time-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd amazon-delivery-time-prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 Requirements

The project uses libraries including:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
mlflow
```

### ⚠️ Scikit-learn Version Compatibility

The saved `.pkl` model is dependent on the Scikit-learn version used during training.

For reliable deployment, use the **same Scikit-learn version for training and running the Streamlit application**.

If the environment versions differ significantly, the saved Pickle model may generate compatibility warnings or loading errors.

---

## 🌍 Live Demo

The Streamlit application is deployed on **Streamlit Community Cloud**.

🔗 **Live Application:**

https://amazon-delivery-time-prediction-7mxnotm73hkh4xva5atbtf.streamlit.app/

---

## 🧠 Key Skills Demonstrated

* Python Programming
* Data Cleaning
* Missing Value Handling
* Exploratory Data Analysis
* Feature Engineering
* Haversine Distance Calculation
* Time-Based Feature Engineering
* One-Hot Encoding
* Regression
* Random Forest
* Gradient Boosting
* Model Evaluation
* Cross-Validation
* MLflow Experiment Tracking
* Model Serialization
* Streamlit Development
* Machine Learning Deployment
* Git & GitHub

---

## ⚠️ Known Limitation

Traffic level has a strong relationship with delivery time in the dataset. However, the Random Forest model does not enforce a strict monotonic relationship between traffic and predicted delivery time.

Because Random Forest learns feature interactions, changing only the traffic level may occasionally produce a counter-intuitive prediction for a specific combination of inputs.

A potential future improvement would be to use a model supporting **monotonic constraints** to enforce expected relationships between selected features and delivery time.

---

## 🚀 Future Enhancements

* Hyperparameter Optimization
* Advanced Ensemble Learning
* Real-Time Weather API Integration
* Real-Time Traffic API Integration
* Geospatial Feature Engineering
* Explainable AI / Feature Importance Dashboard
* Model Monitoring
* Automated MLflow Model Registry
* Cloud-Based MLOps Pipeline
* Prediction Confidence / Uncertainty Estimation

---

## 📌 Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow for a real-world logistics problem.

From cleaning raw delivery data and engineering geographical and time-based features to comparing regression models, tracking experiments with MLflow, selecting the best model, and deploying it through Streamlit, the project showcases how Machine Learning can be applied to practical delivery-time prediction problems.

---

## 👨‍💻 Author

**Himanshu**

B.Tech Student | Machine Learning & Data Science Enthusiast

---

⭐ If you find this project useful, consider giving the repository a star!
