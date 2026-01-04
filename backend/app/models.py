from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# -------------------- Users --------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(20), default="student")
    created_at = Column(DateTime, default=datetime.utcnow)

    submissions = relationship("Submission", back_populates="student")
    tutorial_progress = relationship("TutorialProgress", back_populates="student")


# -------------------- Problems --------------------
class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    difficulty = Column(String(10))

    submissions = relationship("Submission", back_populates="problem")
    tutorials = relationship("Tutorial", back_populates="problem")


# -------------------- Submissions --------------------
class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    code = Column(Text)
    status = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("User", back_populates="submissions")
    problem = relationship("Problem", back_populates="submissions")


# -------------------- Tutorials --------------------
class Tutorial(Base):
    __tablename__ = "tutorials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)   # ✅ Added
    category = Column(String(50), nullable=True) # ✅ Added
    created_at = Column(DateTime, default=datetime.utcnow)

    lessons = relationship("Lesson", back_populates="tutorial")
    problem_id = Column(Integer, ForeignKey("problems.id"), nullable=True)
    problem = relationship("Problem", back_populates="tutorials")
    progress = relationship("TutorialProgress", back_populates="tutorial")


# -------------------- Lessons --------------------
class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    tutorial_id = Column(Integer, ForeignKey("tutorials.id"))
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tutorial = relationship("Tutorial", back_populates="lessons")


# -------------------- Tutorial Progress --------------------
class TutorialProgress(Base):
    __tablename__ = "tutorial_progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorials.id"))
    status = Column(String(20), default="Not Started")
    updated_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("User", back_populates="tutorial_progress")
    tutorial = relationship("Tutorial", back_populates="progress")
