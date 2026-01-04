from fastapi import FastAPI
from .database import engine, Base
from .routers import auth_routes, tutorial_routes
from fastapi.middleware.cors import CORSMiddleware
from . import models

app = FastAPI(title="PyPath Backend")

# -------------------- Enable CORS --------------------
origins = [
    "http://localhost:5173",  # your frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_routes.router)
app.include_router(tutorial_routes.router)

@app.get("/")
def read_root():
    return {"message": "PyPath backend is running!"}
