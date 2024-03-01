from fastapi import FastAPI
from app.api import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
    