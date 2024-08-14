from pydantic import BaseModel
from datetime import date
from typing import List
from patient import Patient

class BillCreate(BaseModel):
    patient_id: int
    date_charged: date
    date: date
    cost_center: int
    cost_name: str
    item_code: int
    description: str
    charge: float

class Bill(BaseModel):
    id: int
    patient_id: int
    date_charged: date
    date: date
    cost_center: int
    cost_name: str
    item_code: int
    description: str
    charge: float

    class Config:
        orm_mode = True

class BillResponse(BaseModel):
    patient: Patient
    bills: List[Bill]

    class Config:
        orm_mode = True
