from pydantic import BaseModel
from typing import List
from .medication import Medication


class Prescription(BaseModel):
    patient_id: str
    medications: List[Medication] = []
