from pydantic import BaseModel


class MedicationInput(BaseModel):
    name: str
    dosage: str
    frequency: str


class Medication(MedicationInput):
    code: int



