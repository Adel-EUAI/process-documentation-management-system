from fastapi import FastAPI
from app.db.database import engine
from app.models import user
from app.routers import auth

app = FastAPI(title="Process Documentation Management API")

user.Base.metadata.create_all(bind=engine)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

@app.get("/")
def root():
    return {"status": "API is running"}
