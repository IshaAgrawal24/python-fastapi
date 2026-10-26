from fastapi import FastAPI, Depends

app = FastAPI()


def get_current_user():
    return "Isha"


@app.get("/profile")
def profile(username: str = Depends(get_current_user)):
    return {
        "status": True,
        "message": "Data fetched successfully!",
        "data": {"id": 1, "username": username},
    }


@app.get("/dashboard")
def dashboard(username: str = Depends(get_current_user)):
    return {
        "status": True,
        "message": "Data fetched successfully!",
        "config": {"id": 1, "username": username},
    }
