from fastapi import FastAPI
from src.db.database import engine
from src.models import user
from src.routers import auth, documents

app = FastAPI(title="Process Documentation Management API")

app.include_router(auth.router)
app.include_router(documents.router)

user.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "API is running"}




