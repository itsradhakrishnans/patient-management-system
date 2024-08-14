from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Bill)
def create_bill(bill_in: schemas.bill.BillCreate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    bill = models.Bill(**bill_in.dict())
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill

@router.get("/{patient_id}", response_model=schemas.bill.BillResponse)
def view_patient_bill(patient_id: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    bills = db.query(models.Bill).filter(models.Bill.patient_id == patient_id).all()
    if not bills:
        raise HTTPException(status_code=404, detail="No bills found for this patient")

    return schemas.bill.BillResponse(patient=patient, bills=bills)
