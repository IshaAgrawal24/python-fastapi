from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    pincode: int
    state: str
    
class User(BaseModel):
    name: str
    age: int
    address: Address #Nested Model
    
users_list: User = []

@app.get("/")
def home():
    return {"message": "This is my home page"}

@app.get("/users")
def users():
    return {
        "message": "Data fetched successully!",
        "data": users_list
    }

@app.post("/ceate-user")
def create_user(user:User):
    users_list.append(user)
    return {
        "return_status": "true",
        "message": "Data fetched successfully!",
        "user": user
    }