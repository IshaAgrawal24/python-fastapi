from fastapi import FastAPI, status, HTTPException

app = FastAPI()

# STATUS CODE 
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User created!"
    }
    
# CUSTOM RESPONSE 
@app.get("/user_list")
def user_list():
    return {
        "status": "Success",
        "message": "Data fetched",
        "data": {
            "name": "Isha",
            "age": 26
        }
    }
    
# ERROR HANDLING BASICS 
@app.get("/user/{id}")
def user(id: int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id": 1,
        "name": "Mohit"
    }