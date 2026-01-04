# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routers import auth_routes, tutorial_routes
# Import models to ensure tables are created
from . import models

app = FastAPI(title="PyPath Backend")

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_routes.router)  # only auth
app.include_router(tutorial_routes.router)

@app.get("/")
def read_root():
    return {"message": "PyPath backend is running!"}
