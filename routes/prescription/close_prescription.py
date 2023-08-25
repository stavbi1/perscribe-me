from fastapi import APIRouter, HTTPException
from DAL.prescriptionDAL import get_prescription, remove_prescription
from BL.prescriptionBL import get_prescription_interaction_warnings

router = APIRouter()


@router.delete("/close/{prescription_id}")
async def close_prescription(prescription_id: int):
    prescription = get_prescription(prescription_id)

    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")

    warnings = await get_prescription_interaction_warnings(prescription)

    remove_prescription(prescription_id)

    return {"message": "Prescription closed", "warnings": warnings}
