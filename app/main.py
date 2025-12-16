from fastapi import FastAPI
from app.db.database import engine
from app.models import user

app = FastAPI(title="Process Documentation Management API")

user.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API is running"}
