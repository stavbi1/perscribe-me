from fastapi import APIRouter
from models.prescription import Prescription
from DAL.prescriptionDAL import insert_prescription

router = APIRouter()


@router.post("/{patient_id}")
def open_prescription(patient_id: str):
    prescription = Prescription(patient_id=patient_id)

    prescription_id = insert_prescription(prescription)

    return {"message": "Prescription opened", "prescription_id": prescription_id}
