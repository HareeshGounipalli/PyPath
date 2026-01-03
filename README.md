# PyPath 🚀

PyPath is a secure, scalable backend platform built using **FastAPI** for managing students, authentication, and future learning workflows.  
It is designed with **clean architecture**, **JWT-based authentication**, and **best security practices**.

This project is built from scratch with simplicity, security, and extensibility in mind.

---

## 📌 Why PyPath?

- Clean backend architecture
- Secure authentication system
- Ready for frontend & mobile apps
- Easy to scale and extend
- Beginner-friendly but production-ready

---

## ✨ Features

### 🔐 Authentication & Security
- User registration
- User login
- JWT access tokens
- Secure password hashing using **Argon2**
- Role-based user model (student by default)

### 🗄️ Database
- PostgreSQL
- SQLAlchemy ORM
- Clean CRUD layer
- Auto timestamps

### 🧱 Architecture
- Modular code structure
- Separation of concerns
- Pydantic v2 schema validation
- Dependency injection

---

## 🧰 Tech Stack

### Backend
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Pydantic v2**
- **Passlib (Argon2)**
- **python-jose (JWT)**

### Tools
- Uvicorn
- Git
- VS Code

---

## 📂 Project Structure

```text
PyPath/
├── backend/
│   ├── app/
│   │   ├── main.py          # App entry point
│   │   ├── auth.py          # Auth, JWT, password hashing
│   │   ├── crud.py          # DB operations
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── database.py     # DB connection
│   │   └── routers/
│   │       └── auth.py      # Auth routes
│   ├── requirements.txt
│   └── venv/
│
├── .gitignore
├── README.md
├── ARCHITECTURE.md
└── .git/
