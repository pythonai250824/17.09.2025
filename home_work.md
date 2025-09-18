# Assignment

## Part 1 – REST API with SQLite

You are given the code in [rest\_list.py](https://github.com/pythonai250824/17.09.2025/blob/master/rest_list.py).
Currently, the logic uses an in-memory Python list. Your task is to **replace it with SQLite queries**.

### Requirements

* **GET /messages**
  Instead of returning the Python list, run:

  ```sql
  SELECT * FROM messages;
  ```
* **GET /messages/{id}**
  Instead of scanning the list, run:

  ```sql
  SELECT * FROM messages WHERE id = ?;
  ```
* **POST /messages**
  Insert a new row into the database:

  ```sql
  INSERT INTO messages (text) VALUES (?);
  ```
* **PUT /messages/{id}**
  Replace the text of an existing row if it exists, otherwise create it:

  ```sql
  UPDATE messages SET text = ? WHERE id = ?;
  ```

  If no row exists → use:

  ```sql
  INSERT INTO messages (id, text) VALUES (?, ?);
  ```
* **PATCH /messages/{id}**
  Update the text only if the row already exists. If not found → return 404.

  ```sql
  UPDATE messages SET text = ? WHERE id = ?;
  ```
* **DELETE /messages/{id}**
  Remove a row from the table:

  ```sql
  DELETE FROM messages WHERE id = ?;
  ```

### Table Creation

Use the following SQL to create the table before running your API:

```sql
CREATE TABLE IF NOT EXISTS messages (
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  text TEXT NOT NULL
);
```

---

## Part 2 – Logistic Regression API

You are given the code in [rest\_linear.py](https://github.com/pythonai250824/17.09.2025/blob/master/rest_linear.py).
Instead of **linear regression**, implement **logistic regression**.

### Example Training Code

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Data: Annual income and loan repayment (1=yes, 0=no)
X = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 1, 0, 1, 1, 1])

# Fit logistic regression model
model = LogisticRegression(solver='liblinear')
model.fit(X, y)

# Coefficients
b0 = model.intercept_[0]
b1 = model.coef_[0][0]

print(f"Logistic regression equation:")
print(f"P(return) = 1 / (1 + e^-({b0:.2f} + {b1:.2f} * income))")
```

### Task

* Implement an endpoint **GET /logistic/predict?x=VALUE**
* When a user sends a request with `x`, return the predicted probability using the trained logistic regression model.

### Function Example

```python
import math

def predict_probability(x: float) -> float:
    z = b0 + b1 * x
    return 1 / (1 + math.exp(-z))
```

### Example Response

```json
{
  "x": 55,
  "probability": 0.73
}
```

### submit solution 
to: pythonai250824+hwrest1@gmail.com
