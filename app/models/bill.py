from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from patient import Patient

class Bill(Base):
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patient.id"))
    date = Column(Date)
    cost_center = Column(Integer)
    cost_name = Column(String)
    date_charged = Column(Date)
    item_code = Column(Integer)
    description = Column(String)
    charge = Column(Float)
    patient = relationship("Patient", back_populates="bills")

Patient.bills = relationship("Bill", back_populates="patient")
