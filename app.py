import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

# Load Model

with open("xgb_tuned_model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("🏠 House Price Prediction using XGBoost")

st.sidebar.header("Enter House Details")

bedrooms = st.sidebar.number_input("Number of Bedrooms", 0, 20, 3)
bathrooms = st.sidebar.number_input("Number of Bathrooms", 0.0, 10.0, 2.0)
living_area = st.sidebar.number_input("Living Area", 100, 20000, 1500)
lot_area = st.sidebar.number_input("Lot Area", 500, 100000, 5000)
floors = st.sidebar.number_input("Number of Floors", 1, 5, 1)
waterfront = st.sidebar.selectbox("Waterfront Present", [0, 1])
views = st.sidebar.slider("Number of Views", 0, 10, 0)
condition = st.sidebar.slider("Condition of House", 1, 5, 3)
grade = st.sidebar.slider("Grade of House", 1, 10, 7)
area_no_basement = st.sidebar.number_input("Area excluding Basement", 100, 20000, 1200)
basement_area = st.sidebar.number_input("Basement Area", 0, 10000, 0)
built_year = st.sidebar.number_input("Built Year", 1900, 2025, 2000)
renovation_year = st.sidebar.number_input("Renovation Year (0 if none)", 0, 2025, 0)
latitude = st.sidebar.number_input("Latitude", -90.0, 90.0, 47.5)
longitude = st.sidebar.number_input("Longitude", -180.0, 180.0, -122.0)
living_area_renov = st.sidebar.number_input("Living Area Renovated", 100, 20000, 1500)
lot_area_renov = st.sidebar.number_input("Lot Area Renovated", 500, 100000, 5000)

input_data = np.array([[  
    bedrooms,
    bathrooms,
    living_area,
    lot_area,
    floors,
    waterfront,
    views,
    condition,
    grade,
    area_no_basement,
    basement_area,
    built_year,
    renovation_year,
    latitude,
    longitude,
    living_area_renov,
    lot_area_renov
]])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Price: ₹ {prediction:,.2f}")