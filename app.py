import streamlit as st
import joblib
import time

# Load model
model = joblib.load('rating_prediction_model.pkl')

# ---- APP CONFIGURATION ----
st.set_page_config(page_title="Restaurant Rating Predictor", page_icon="🍽️", layout="centered")

# ---- CUSTOM CSS ----
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff6f61;
        color: white;
    }
    .stRadio > div { 
        display: flex; 
        gap: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER ----
st.markdown(
    """
    <h1 style="text-align: center; color: #ff4b4b;">🍽️ Restaurant Rating Predictor 🍽️</h1>
    <p style="text-align: center; color: #d3d3d3;">
    Predict the rating of a restaurant based on its features!
    </p>
    """,
    unsafe_allow_html=True
)

# ---- INPUT SECTION ----
st.subheader("🔎 Enter Details Below 👇")

# Country Code - Dropdown with Tooltip
country = st.selectbox(
    "🌍 Country Code",
    options=[1, 2, 3, 4, 5],
    index=0,
    help="Select the country code where the restaurant is located."
)

# Price Range - Slider with Tooltip
price_range = st.slider(
    "💰 Price Range",
    min_value=1,
    max_value=4,
    value=2,
    help="1 = Low, 4 = High"
)

# Cuisine Code - Dropdown with Tooltip
cuisine = st.selectbox(
    "🍲 Cuisine Code",
    options=[1, 2, 3, 4, 5, 6, 7],
    index=0,
    help="Select the type of cuisine served."
)

# Online Delivery - Radio Button with Tooltip
online_delivery = st.radio(
    "🚚 Online Delivery",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No",
    help="0 = No delivery, 1 = Delivery available"
)

# ---- BUTTONS ----
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Predict Rating"):
        with st.spinner('✨ Predicting...'):
            try:
                # Simulate processing time for better UX
                time.sleep(1.5)
                prediction = model.predict([[country, price_range, cuisine, online_delivery]])
                st.success(f'⭐ Predicted Rating: {prediction[0]:.2f}')
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error: {e}")

with col2:
    if st.button("🔄 Reset"):
        st.experimental_rerun()

# ---- FOOTER ----
st.markdown(
    """
    <hr>
    <p style="text-align: center; font-size: 14px; color: #888;">
    Developed with ❤️ by <strong>RajibLochan Pramanik</strong> | Happy Coding😎
    </p>
    """,
    unsafe_allow_html=True
)
