from fastapi import FastAPI, Query
from sklearn.linear_model import LinearRegression
import numpy as np
from starlette.responses import HTMLResponse

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
def get_prediction(x: float = 0):
    result = float(model.predict(np.array([[x]], dtype=float))[0])
    return {
        "x": x,
        "y_pred": result
    }

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>My Home Page</title>
        </head>
        <body>
            <h1>Welcome to my FastAPI Home Page 🚀</h1>
            <p>This is served with FastAPI</p>
            <a href="./linear/predict">predict url </a>
        </body>
    </html>
    """

# to run:
# in the Terminal:
# uvicorn rest_linear:app --port 9001 --reload