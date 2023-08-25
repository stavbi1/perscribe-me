from fastapi import APIRouter, HTTPException
from DAL.prescriptionDAL import get_prescription
from DAL.medicationDAL import add_medication
from models.medication import Medication, MedicationInput
from BL.medicationBL import validate_medication

router = APIRouter()


@router.post("/{prescription_id}")
async def add_medication_to_prescription(prescription_id: int, medication_input: MedicationInput):
    prescription = get_prescription(prescription_id)

    if not prescription:
        raise HTTPException(status_code=404, detail="Prescription not found")

    medication_code = await validate_medication(medication_input.name, medication_input.dosage)

    if not medication_code:
        raise HTTPException(status_code=404, detail="a medication with this dosage was not found")

    medication = Medication(
        code=medication_code,
        **medication_input.dict()
    )

    add_medication(prescription_id, medication)

    return {"message": "Medication added to prescription"}
