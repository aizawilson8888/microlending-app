# app/main.py
from fastapi import FastAPI
from app import models

app = FastAPI(title="Microlending App")

@app.get("/")
def read_root():
    return {"message": "Welcome to Microlending App"}

# Borrower endpoints
@app.post("/borrowers")
def create_borrower(borrower: models.Borrower):
    # Logic to save borrower
    return {"status": "Borrower created"}

# Investor endpoints
@app.post("/investors")
def create_investor(investor: models.Investor):
    return {"status": "Investor created"}

# Loan endpoints
@app.post("/loans")
def request_loan(loan: models.Loan):
    return {"status": "Loan requested"}
