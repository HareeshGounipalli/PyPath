# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import auth_routes  # add routers

# Import models to ensure tables are created
from . import models

app = FastAPI(title="PyPath Backend")

# Create tables
Base.metadata.create_all(bind=engine)

# Include auth routes
app.include_router(auth_routes.router)

@app.get("/")
def read_root():
    return {"message": "PyPath backend is running!"}
