# 📊 AI Analytics Dashboard

Live Demo 👉 https://ai-analytics-dashboard-2wonyrv4mc6feddsu2d2mi.streamlit.app/

An **end-to-end AI-powered analytics dashboard** built using **Python, Streamlit, and Scikit-learn**.  
This project accepts *any CSV*, runs ML modeling automatically, and displays **interactive insights & visualizations** for business decision support.

---

## 🚀 Live Demo

Try the live version of the app here:  
🔗 https://ai-analytics-dashboard-2wonyrv4mc6feddsu2d2mi.streamlit.app/

Upload any CSV with numeric columns and explore analytics instantly.

---

## 🔥 Features

✔ Upload ANY CSV file  
✔ Auto ML model training  
✔ KPI dashboard (Total, Average, Best, Count)  
✔ Performance Trend (rolling average)  
✔ Actual vs Predicted plot  
✔ Target distribution & Residual analysis  
✔ Model performance metrics (MSE, RMSE, R²)  
✔ Interactive executive summary  
✔ Fast caching and deployment-ready UI

---

## 🧠 Machine Learning Details

**Regression Model:** Random Forest Regressor  
**Preprocessing:**  
- Numeric columns → Standard Scaling  
- Categorical columns → One-Hot Encoding  
**Evaluation Metrics:**  
- MSE (Mean Squared Error)  
- RMSE (Root Mean Squared Error)  
- R² Score

---

## 🗂️ Project Structure

AI-Analytics-Dashboard/
*│
*├── app.py
*├── requirements.txt
*├── README.md
*│
*├── utils/
*│ ├── init.py
*│ ├── data_loader.py
*│ ├── preprocessing.py
*│ ├── model.py
*│ ├── visualization.py
*│ └── summary.py
*│
*└── .streamlit/
*└── config.toml


---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-Analytics-Dashboard.git
cd AI-Analytics-Dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py


Open in browser:

http://localhost:8501

📊 Example Use Cases

Business KPI tracking

Sales & revenue forecasting

Educational performance analysis

Healthcare cost modeling

General AutoML analytics for CSV datasets

💼 Skills Highlight

This project demonstrates:
*✔ Python & data handling
*✔ ML modeling with Scikit-Learn
*✔ Interactive dashboards with Streamlit
*✔ Data visualization with Plotly
*✔ AutoML pipeline design
*✔ Live cloud deployment

🧪 Suggested Test Datasets

You can test the app with:

Students Performance data

House Prices Dataset

Superstore / Sales data

Medical Insurance Cost data

Car Prices dataset

(All are publicly available on Kaggle)

📈 Future Improvements

Classification model support

Time-series forecasting

Custom report exports (PDF/CSV)

Deployment with CI/CD pipelines

User authentication & multi-user support

👤 Author

Indar Singh Rajawat
