# app/models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
from sqlalchemy.sql import func

# -------------------- Users Table --------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(20))  # "student", "teacher", "admin"
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    submissions = relationship("Submission", back_populates="student")
    draft_codes = relationship("DraftCode", back_populates="student")
    tutorial_progress = relationship("TutorialProgress", back_populates="student")
    audit_logs = relationship("AuditLog", back_populates="user")


# -------------------- Problems Table --------------------
class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    difficulty = Column(String(10))  # "Easy", "Medium", "Hard"

    # Relationships
    submissions = relationship("Submission", back_populates="problem")
    draft_codes = relationship("DraftCode", back_populates="problem")
    tutorials = relationship("Tutorial", back_populates="problem")


# -------------------- Submissions Table --------------------
class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    code = Column(Text)
    status = Column(String(50))  # "Not Started", "In Progress", "Solved", etc.
    score = Column(Integer, default=0)
    execution_time = Column(Integer)  # in milliseconds
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("User", back_populates="submissions")
    problem = relationship("Problem", back_populates="submissions")


# -------------------- DraftCode Table --------------------
class DraftCode(Base):
    __tablename__ = "draft_code"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    code = Column(Text)
    last_updated_by = Column(String(100))
    updated_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("User", back_populates="draft_codes")
    problem = relationship("Problem", back_populates="draft_codes")


# -------------------- Tutorials Table --------------------
class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)  # Markdown content
    category = Column(String(50))  # e.g., "Python Basics", "OOP"
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable=True)

    # Relationships
    problem = relationship("Problem", back_populates="tutorials")
    progress = relationship("TutorialProgress", back_populates="tutorial")


# -------------------- TutorialProgress Table --------------------
class TutorialProgress(Base):
    __tablename__ = "tutorial_progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorials.id"))
    status = Column(String(20), default="Not Started")  # "Not Started", "In Progress", "Completed"
    updated_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("User", back_populates="tutorial_progress")
    tutorial = relationship("Tutorial", back_populates="progress")


# -------------------- AuditLogs Table --------------------
class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String(255))
    details = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="audit_logs")

class Tutorial(Base):
    __tablename__ = "tutorials"
    __table_args__ = {"extend_existing": True}  # <-- Add this line

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
