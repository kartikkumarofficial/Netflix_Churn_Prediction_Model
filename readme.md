# 🎬 Netflix Churn Prediction Model

A production-ready **Machine Learning churn prediction system** that predicts whether a Netflix customer is likely to churn based on behavioral, subscription, and engagement signals.

🔗 **Live Demo:** https://netflixchurnpredictionmodel.streamlit.app/

---

## 🚀 Project Overview

Customer churn is one of the most critical business problems for subscription-based platforms like Netflix.

This project uses **Machine Learning + behavioral analytics** to identify users at risk of leaving the platform and provides actionable retention insights.

The system analyzes:

- 👤 User demographics
- 📺 Viewing behavior
- ⏳ Platform inactivity
- 💳 Payment patterns
- 👨‍👩‍👧 Account usage behavior
- 🎭 Content preferences

and predicts:

- ✅ Churn / No Churn
- 📊 Churn probability %
- 🚨 Risk level
- 💡 Suggested retention actions

---

## 🎯 Business Problem

Subscription platforms lose revenue when users silently disengage.

This model helps answer:

> **Which users are most likely to cancel their subscription?**

By predicting churn early, platforms can take actions like:

- Personalized content recommendations
- Discount offers
- Engagement notifications
- Subscription downgrade suggestions
- Win-back campaigns

---

## 🧠 ML Pipeline

The project follows a **production-grade ML workflow**:

### ✅ Data Preprocessing
- Removed non-informative identifiers (`customer_id`)
- Train-test split with stratification
- `ColumnTransformer`
- `OneHotEncoder` for categorical features
- Standardization for numerical features
- Full `Pipeline` integration

### ✅ Models Compared
- Logistic Regression
- Decision Tree
- XGBoost

### 🏆 Final Model
**XGBoost Classifier**

Cross-validation F1-score: **0.99**

---

## 📊 Key Churn Drivers

Top features influencing churn:

- `avg_watch_time_per_day`
- `payment_method_Crypto`
- `monthly_fee`
- `last_login_days`
- `watch_hours`
- `number_of_profiles`

### 💡 Major Insight
Daily watch time emerged as the strongest churn predictor, contributing nearly **47% feature importance**, indicating that user engagement is the strongest retention signal.

---

## 🖥️ Deployment

The project is deployed using **Streamlit Cloud**.

🔗 **Live App:** https://netflixchurnpredictionmodel.streamlit.app/

### Features of the deployed app
- 🎛️ Interactive customer input form
- 📊 Real-time churn probability
- 🚦 Risk level classification
- 💡 Retention recommendations
- ⚡ Instant prediction using saved ML pipeline

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Streamlit
- Joblib

---

## 📁 Project Structure

```bash
Netflix-Churn-Prediction/
│
├── models/
│   └── netflix_churn_pipeline.pkl
│
├── notebook/
│   └── churn_model.ipynb
│
├── app/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

### 1️⃣ Clone repository
```bash
git clone https://github.com/your-username/netflix-churn-prediction.git
cd netflix-churn-prediction
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit app
```bash
streamlit run app/app.py
```

---

## 📈 Results

| Model | F1 Score |
|---|---:|
| Logistic Regression | 0.89 |
| Decision Tree | 0.97 |
| XGBoost | **0.99** |

---

## 🚀 Future Improvements

- FastAPI inference backend
- Dockerized deployment
- SHAP explainability dashboard
- Batch churn scoring
- User segmentation with clustering
- Personalized retention engine
- Flutter frontend integration

---

## 💼 Why This Project Matters

This project demonstrates:

- ✅ End-to-end ML pipeline design
- ✅ Feature engineering & business insights
- ✅ Model comparison and evaluation
- ✅ Production deployment
- ✅ Real-world churn use case
- ✅ Product thinking with retention strategies

---

## 👨‍💻 Author

**Kartik Kumar**  
AI/ML • Flutter • Data Science

If you like this project, feel free to ⭐ the repository.