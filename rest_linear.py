from fastapi import FastAPI, Query
from sklearn.linear_model import LinearRegression
import numpy as np

app = FastAPI(title="Linear Regression via GET /messages")

# --- Train a simple model at startup ---
# Toy training data: y ≈ 2.5*x + 1
X_train = np.array([[0], [1], [2], [3], [4], [5]], dtype=float)
y_train = np.array([1, 3.5, 6, 8.5, 11, 13.5], dtype=float)

model = LinearRegression()
model.fit(X_train, y_train)

coef = float(model.coef_[0])  # a
intercept = float(model.intercept_)  # b

@app.get("/linear/predict")
def get_prediction(x: float):
    result = float(model.predict(np.array([[x]], dtype=float))[0])
    return {
        "x": x,
        "y_pred": result
    }