from sqlalchemy import Column, Integer, String, Date
from app.db.base_class import Base

class Patient(Base):
    id = Column(Integer, primary_key=True, index=True)
    patient_number = Column(String, unique=True, index=True)
    name = Column(String)
    address = Column(String)
    city_state_zip = Column(String)
    date_admitted = Column(Date)
    discharge_date = Column(Date)
