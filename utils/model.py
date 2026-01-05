import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

@st.cache_resource
def get_model():
    return RandomForestRegressor(
        n_estimators=120,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )

def run_regression(X_train, X_test, y_train, y_test):
    model = get_model()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    return {
        "y_pred": y_pred,
        "mse": mse,
        "rmse": rmse,
        "r2": r2,
        "future_prediction": float(y_pred[0])
    }
