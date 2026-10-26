from fastapi import FastAPI, Header, Depends, HTTPException

app = FastAPI()

#  TO CHECK WETHER THE TOKEN IS AUTHORISED OR NOT.........  T
def varify_token(token: str):
    if token != "MySecretToken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorised token"
        )
    return {
        "user": "Authorized!"
    }
    
@app.get("/config")
def config(token: str = Depends(varify_token)):
    return {
        "status": True,
        "message": "User verified",
        "data": token
    }