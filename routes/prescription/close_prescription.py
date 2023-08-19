from fastapi import APIRouter, HTTPException
from DAL.prescriptionDAL import get_prescription, remove_prescription

router = APIRouter()


@router.put("/close/{prescription_id}")
def close_prescription(prescription_id: int):
    prescription = get_prescription(prescription_id)

    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")

    remove_prescription(prescription_id)

    return {"message": "Prescription closed"}
