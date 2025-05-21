from fastapi import FastAPI
from app.routes import spam

app = FastAPI(title="Spam Detection API")

app.include_router(spam.router)
