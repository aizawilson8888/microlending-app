# app/models.py
from pydantic import BaseModel
from datetime import date

# Pydantic models for request validation
class Borrower(BaseModel):
    name: str
    email: str
    role: str  # e.g., "borrower" or "investor"

class Investor(BaseModel):
    name: str
    email: str

class Loan(BaseModel):
    borrower_id: int
    amount: float
    interest: float
    due_date: date

# Optional: SQLAlchemy ORM models for PostgreSQL
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BorrowerDB(Base):
    __tablename__ = "borrowers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

class LoanDB(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    borrower_id = Column(Integer)
    amount = Column(Float)
    interest = Column(Float)
    due_date = Column(Date)
