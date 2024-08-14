from fastapi import FastAPI
from api.endpoints import auth, patients, bills
from app.db import base, session


app = FastAPI()

base.Base.metadata.create_all(bind=session.engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(bills.router, prefix="/bills", tags=["bills"])
