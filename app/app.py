import streamlit as st
import joblib
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Netflix Churn Predictor",
    page_icon="🎬",
    layout="centered"
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load("models/netflix_churn_pipeline.pkl")

model = load_model()

# UI
st.title("🎬 Netflix Churn Predictor")
st.write("Predict whether a customer is likely to churn.")

st.subheader("📋 Customer Information")

# Numerical Inputs
age = st.number_input("Age", min_value=10, max_value=100, value=25)
watch_hours = st.slider("Watch Hours", 0, 100, 20)
last_login_days = st.slider("Last Login Days", 0, 60, 5)
monthly_fee = st.number_input("Monthly Fee", min_value=0.0, max_value=1000.0, value=199.0)
number_of_profiles = st.slider("Number of Profiles", 1, 5, 2)
avg_watch_time_per_day = st.slider("Avg Watch Time Per Day (hrs)", 0.0, 10.0, 2.0)

# Categorical Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
subscription_type = st.selectbox(
    "Subscription Type",
    ["Basic", "Standard", "Premium"]
)
region = st.selectbox(
    "Region",
    ["India", "USA", "UK", "Canada", "Europe"]
)
device = st.selectbox(
    "Primary Device",
    ["Mobile", "Laptop", "TV", "Tablet"]
)
payment_method = st.selectbox(
    "Payment Method",
    ["Credit Card", "Debit Card", "PayPal", "Crypto", "Gift Card"]
)
favorite_genre = st.selectbox(
    "Favorite Genre",
    ["Action", "Drama", "Comedy", "Sci-Fi", "Horror", "Romance"]
)

# Prediction

if st.button("🔮 Predict Churn"):
    input_df = pd.DataFrame([{
        "age": age,
        "gender": gender,
        "subscription_type": subscription_type,
        "watch_hours": watch_hours,
        "last_login_days": last_login_days,
        "region": region,
        "device": device,
        "monthly_fee": monthly_fee,
        "payment_method": payment_method,
        "number_of_profiles": number_of_profiles,
        "avg_watch_time_per_day": avg_watch_time_per_day,
        "favorite_genre": favorite_genre
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    prob_percent = probability * 100

    st.subheader("📊 Prediction Result")

    # Risk level logic
    if prob_percent < 20:
        risk = "🟢 Low Risk"
        st.success(f"{risk} — Churn Probability: {prob_percent:.2f}%")
    elif prob_percent < 60:
        risk = "🟡 Medium Risk"
        st.warning(f"{risk} — Churn Probability: {prob_percent:.2f}%")
    else:
        risk = "🔴 High Risk"
        st.error(f"{risk} — Churn Probability: {prob_percent:.2f}%")

    # Business recommendation
    st.subheader("💡 Suggested Retention Action")

    if prob_percent >= 60:
        st.write("👉 Offer personalized content recommendations and subscription discounts.")
    elif prob_percent >= 20:
        st.write("👉 Send engagement notifications and trending show reminders.")
    else:
        st.write("👉 User is stable. Continue personalized recommendations.")