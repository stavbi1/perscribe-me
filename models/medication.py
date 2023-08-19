from pydantic import BaseModel
from typing import List


class MedicationInput(BaseModel):
    name: str
    dosage: str
    frequency: str


class Medication(MedicationInput):
    codes: List[int] = None



