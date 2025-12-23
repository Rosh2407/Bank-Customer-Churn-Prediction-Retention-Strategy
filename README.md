# 🏦 Bank Customer Churn Prediction & Retention Analytics

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)

## 📊 Business Overview
The goal of this project was to identify high-risk customers likely to leave the bank and quantify the financial impact of churn. By predicting churn accurately, the bank can implement proactive retention strategies to save millions in deposits.

### 💰 Key Financial Impact
- **Total Value at Risk:** Identified **$[Insert Your Value]** in account balances belonging to customers likely to churn.
- **Potential Revenue Saved:** By targeting these customers with a 20% success rate, the bank can retain an estimated **$[Insert Your Value]** annually.

## 🚀 Live Demo
**[Click Here to Access the Live Predictor App]([https://bank-customer-churn-prediction-retention-strategy-roshan.streamlit.app/])**

## 🔍 Major Insights (EDA)
* **The Mid-Age Crisis:** Customers in the **45-60 age bracket** show a **50% churn rate**, making them the highest-risk demographic.
* **High-Value Leakage:** Customers with credit scores >700 and balances >$100k churn at a rate of **25%**, which is significantly higher than the 20% average for standard customers.
* **Engagement Matters:** Inactive members with credit cards are far more likely to leave than active members, suggesting that product ownership alone doesn't guarantee loyalty.

## 🛠️ Technical Implementation
### 1. Data Pipeline
- Built a robust **Scikit-Learn Pipeline** to handle scaling, one-hot encoding, and model training simultaneously to prevent data leakage.
- Addressed class imbalance using a **Random Forest Classifier**, which outperformed baseline logistic regression.

### 2. Model Performance
| Metric | Score |
| :--- | :--- |
| **Accuracy** | 87% |
| **Precision (Churn)** | 75% |
| **Recall (Churn)** | 47% |

> *Note: We prioritized Precision to ensure that retention budget is spent on customers truly at risk.*

## 📂 Repository Structure
- `app.py`: Streamlit web application code.
- `churn_model.pkl`: Serialized Random Forest pipeline.
- `requirements.txt`: Necessary libraries for deployment.
- `Notebook.ipynb`: Full EDA and Model training workflow.

## 🤝 Contact
- **LinkedIn:** [[Roshan Madake](https://www.linkedin.com/in/roshanmadake2407)]
