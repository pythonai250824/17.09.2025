from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simple in-memory "database"
messages = [
    {"id": 1, "text": "First message"},
    {"id": 2, "text": "Second message"}
]

# GET all
@app.get("/messages")
def get_messages():
    return messages

# GET by id
@app.get("/messages/{id}")
def get_message(id: int):
    for msg in messages:
        if msg["id"] == id:
            return msg
    raise HTTPException(status_code=404, detail="Message not found")

# POST (create new)
@app.post("/messages")
def create_message(text: str):
    new_id = max([m["id"] for m in messages], default=0) + 1
    new_msg = {"id": new_id, "text": text}
    messages.append(new_msg)
    return new_msg

# PUT (replace or create)
@app.put("/messages/{id}")
def put_message(id: int, text: str):
    for msg in messages:
        if msg["id"] == id:
            msg["text"] = text
            return msg
    # if not found, create
    new_msg = {"id": id, "text": text}
    messages.append(new_msg)
    return new_msg

# PATCH (update only if exists)
@app.patch("/messages/{id}")
def patch_message(id: int, text: str):
    for msg in messages:
        if msg["id"] == id:
            msg["text"] = text
            return msg
    raise HTTPException(status_code=404, detail="Message not found")

# DELETE
@app.delete("/messages/{id}")
def delete_message(id: int):
    for i, msg in enumerate(messages):
        if msg["id"] == id:
            return messages.pop(i)
    raise HTTPException(status_code=404, detail="Message not found")
