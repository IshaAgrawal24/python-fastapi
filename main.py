from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    status: Literal["Completed" , "Pending" , "In Process"]
    
class TodoUpdate(BaseModel):
    title: str
    status: Literal["Completed" , "Pending" , "In Process"]
    
todos: Todo = []

# TODO - LIST 
@app.get("/todo-list")
def todo_list():
    return {
        "return_status": 200,
        "message": "Data fetched successfully!",
        "data": todos
    }
    
# FILTER THE TODO LIST 
@app.get("/todo/{id}")
def find_todo(id: int):
    for task in todos:
        if task.id == id:
            return {
                "return_status": 200,
                "message": "Data fetched successfully!",
                "data": task
            }
    return {"error": "ID not found"}        

# CREATE A TODO TASK
@app.post("/create-todo")
def ceate_todo(todo: Todo):
    todos.append(todo)
    return {
        "return_status": 201,
        "message": "Data created successfully!",
        "data": todo
    }
    
# EDIT THE TODO TASK 
@app.put("/edit-todo/{id}")
def edit_todo(id: int, updated_task: TodoUpdate):
    for index, task in enumerate(todos):
        if task.id == id:
            task.title = updated_task.title
            task.status = updated_task.status
            return {
                "return_status": 200,
                "message": "Data updated successfully!",
                "data": task
            }
    return {"error": "ID not found"}    

# DELETE A TODO TASK 
@app.delete("/remove-todo/{id}")
def remove_todo(id: int):
    for index, task in enumerate(todos):
        if task.id == id:
            deleted_task = todos.pop(index)
            return {
                "return_status": 200,
                "message": "Data deleted successfully!",
                "data": deleted_task
            } 
    return {"error": "ID not found"}   

