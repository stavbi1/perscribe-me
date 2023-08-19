from pydantic import BaseModel
from typing import Dict
from models.prescription import Prescription


class PrescriptionDB(BaseModel):
    prescriptions: Dict[int, Prescription] = {}
    lastIndex: int = 0

    def next_index(self):
        self.lastIndex = self.lastIndex + 1
        return self.lastIndex - 1


prescriptions_db = PrescriptionDB()


