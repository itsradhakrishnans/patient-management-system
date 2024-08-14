from pydantic import BaseModel
from datetime import date

class PatientCreate(BaseModel):
    patient_number: str
    name: str
    address: str
    city_state_zip: str
    date_admitted: date
    discharge_date: date

class Patient(BaseModel):
    id: int
    patient_number: str
    name: str
    address: str
    city_state_zip: str
    date_admitted: date
    discharge_date: date

    class Config:
        orm_mode = True
