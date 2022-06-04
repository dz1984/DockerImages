from typing import Union
from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def get_index():
	return {"message": "FastAPI is runing."}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, q: Union[str, None] = None):
	return {"todo_id": todo_id, "q": q}