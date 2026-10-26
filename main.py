from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, id: int):
        self.id = id

# GLOBAL EXCEPTION 
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "Error",
            "message": f"User {exc.id} not found!"
        }
    )


# CUSTOM EXCEPTION 
@app.get("/user/{id}")
def user_data(id: int):
    if id != 1:
        raise UserNotFoundException(id)
    return {
        "status": True,
        "message": "Data fetched successfully",
        "data": [{
            "id": 1,
            "name": "Isha"
        }]
    }
    
    
    
    
    
# HTTPException is a built in error handling function................
   
# @app.get("/user/{id}")
# def user_data(id: int):
#     if id != 1:
#         raise HTTPException(
#             status_code= 404,
#             detail= "User not found" 
#         )
#     return {
#         "status": 200,
#         "data": {
#             "id": 1,
#             "name": "Isha"
#         }
#     }    