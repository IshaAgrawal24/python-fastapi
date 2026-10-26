from fastapi import FastAPI, Request
import time

app = FastAPI()


# LOGGING MIDDLEWARE 
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time  = time.time() - start_time
    print(f"request path: {request.url.path} | Process TIme: {process_time}")
    return response
