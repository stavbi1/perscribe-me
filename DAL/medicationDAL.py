from .db import prescriptions_db
from models.medication import Medication


def add_medication(prescription_id: int, medication: Medication):
    prescriptions_db.prescriptions[prescription_id].medications.append(medication)