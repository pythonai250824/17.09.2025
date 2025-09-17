
from fastapi import FastAPI
import uvicorn

# Create the app
app = FastAPI()
# Starlette
# Flask
# Django

# http://127.0.0.1:8000
# 8000 PORT

# REST API
# GET    -- read from
# POST   -- insert into db (create)
# PUT    -- create/update {like dict in python a['age'] = 18}
# PATCH  -- update {if not exist, error}
# DELETE -- delete

# Root endpoint
@app.get("/messages")
def read_root():
    return {"message": "Hello, GET"}

@app.get("/messages/{id}")
def read_root(id: int):
    return {"message": "Hello,GET by ID!~!!!!!!!!!!!!!"}

@app.post("/messages")
def read_root():
    return {"message": "Hello, POST"}

@app.put("/messages/{id}")
def read_root(id: int):
    return {"message": "Hello, PUT"}

@app.patch("/messages/{id}")
def say_hello(id: int):
    return {"message": f"Hello, PATCH"}

@app.delete("/messages/{id}")
def say_hello(id: int):
    return {"message": f"Hello, DELETE!"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=9001, reload=True)

# to run:
# in the Terminal:
# uvicorn main:app --port 9001 --reload