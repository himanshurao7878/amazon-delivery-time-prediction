# app.py — Amazon Delivery Time Prediction (Final Version)

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from datetime import datetime

# =============================
# Load Trained Model
# =============================
with open("best_delivery_model.pkl", "rb") as f:
    model = pickle.load(f)

# =============================
# Streamlit Config
# =============================
st.set_page_config(page_title="Amazon Delivery Time Prediction", page_icon="📦", layout="centered")
st.title("📦 Amazon Delivery Time Prediction")
st.markdown("### 🚀 Predict how long a delivery will take based on real-world conditions.")
st.write("---")

# =============================
# Sidebar
# =============================
st.sidebar.header("ℹ️ Project Information")
st.sidebar.markdown("""
**Project:** Amazon Delivery Time Prediction  
**Goal:** Predict delivery duration (in hours)  
**Tech Stack:** Python, Scikit-learn, MLflow, Streamlit  
**Best Model:** Gradient Boosting Regressor ✅  

**Performance (Test Set):**  
- MAE ≈ 30.5  
- RMSE ≈ 41.1  
- R² ≈ 0.37  
""")

# =============================
# User Inputs
# =============================
st.header("🧠 Enter Delivery Details")

col1, col2 = st.columns(2)
with col1:
    distance = st.number_input("Distance (km)", min_value=0.1, max_value=100.0, value=5.0, step=0.1)
    agent_age = st.number_input("Agent Age", min_value=18, max_value=65, value=30)
    agent_rating = st.slider("Agent Rating (1–5)", 1.0, 5.0, 4.5, 0.1)
    order_date = st.date_input("Order Date", value=datetime.today())
with col2:
    order_time = st.time_input("Order Time", value=datetime.now().time())
    weather = st.selectbox("Weather Condition", ["Sunny", "Fog", "Cloudy", "Stormy", "Windy", "Sandstorms"])
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "Jam"])
    vehicle = st.selectbox("Vehicle Type", ["motorcycle", "scooter", "van"])
    area = st.selectbox("Delivery Area", ["Urban", "Semi-Urban", "Other"])
    category = st.selectbox("Product Category", [
        "Books", "Clothing", "Cosmetics", "Electronics", "Grocery", "Home", "Jewelry",
        "Kitchen", "Outdoors", "Pet Supplies", "Shoes", "Skincare", "Snacks", "Sports", "Toys"
    ])

st.write("---")

# =============================
# Feature Engineering (same as Day 1 pipeline)
# =============================

def create_feature_vector():
    data = {
        "Agent_Age": [agent_age],
        "Agent_Rating": [agent_rating],
        "Distance_km": [distance],
        "Order_Hour": [order_time.hour],
        "Order_Weekday": [order_date.weekday()],
        "Is_Weekend": [1 if order_date.weekday() >= 5 else 0],
    }

    # Base DF
    df = pd.DataFrame(data)

    # One-hot encoded categorical columns (aligning with training set)
    weather_cols = ['Weather_Cloudy', 'Weather_Fog', 'Weather_Sandstorms',
                    'Weather_Stormy', 'Weather_Sunny', 'Weather_Windy']
    traffic_cols = ['Traffic_Jam ', 'Traffic_Low ', 'Traffic_Medium ', 'Traffic_NaN ']
    vehicle_cols = ['Vehicle_motorcycle ', 'Vehicle_scooter ', 'Vehicle_van']
    area_cols = ['Area_Other', 'Area_Semi-Urban ', 'Area_Urban ']
    category_cols = [
        'Category_Books', 'Category_Clothing', 'Category_Cosmetics', 'Category_Electronics',
        'Category_Grocery', 'Category_Home', 'Category_Jewelry', 'Category_Kitchen',
        'Category_Outdoors', 'Category_Pet Supplies', 'Category_Shoes', 'Category_Skincare',
        'Category_Snacks', 'Category_Sports', 'Category_Toys'
    ]

    # Initialize all to 0
    for col in weather_cols + traffic_cols + vehicle_cols + area_cols + category_cols:
        df[col] = 0

    # Activate the selected ones
    df[f"Weather_{weather}"] = 1
    df[f"Traffic_{traffic} "] = 1
    df[f"Vehicle_{vehicle} "] = 1
    df[f"Area_{area} "] = 1
    df[f"Category_{category}"] = 1

    # Add placeholders for columns not used directly
    df["Drop_Latitude"] = 0.0
    df["Drop_Longitude"] = 0.0
    df["Store_Latitude"] = 0.0
    df["Store_Longitude"] = 0.0

    # Ensure correct column order
    expected_columns = model.feature_names_in_
    df = df.reindex(columns=expected_columns, fill_value=0)

    return df

# =============================
# Predict
# =============================
if st.button("🔮 Predict Delivery Time"):
    try:
        input_vector = create_feature_vector()
        prediction = model.predict(input_vector)[0]
        st.success(f"⏱️ Estimated Delivery Time: **{prediction:.2f} hours**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")

st.write("---")
st.caption("Built with ❤️ using Streamlit and Scikit-learn")
