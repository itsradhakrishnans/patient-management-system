from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.Patient)
def create_patient(patient_in: schemas.patient.PatientCreate, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    patient = models.Patient(**patient_in.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/{patient_id}", response_model=schemas.patient.Patient)
def view_patient(patient_id: int, db: Session = Depends(deps.get_db), current_user: models.User = Depends(deps.get_current_user)):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
