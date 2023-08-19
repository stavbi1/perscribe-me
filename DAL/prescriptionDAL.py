from models.prescription import Prescription
from .db import prescriptions_db


def insert_prescription(prescription: Prescription):
    prescription_id = prescriptions_db.next_index()
    prescriptions_db.prescriptions[prescription_id] = prescription

    print(prescriptions_db)

    return prescription_id


def get_prescription(prescription_id):
    if prescription_id < len(prescriptions_db.prescriptions):
        return prescriptions_db.prescriptions[prescription_id]


def remove_prescription(prescription_id):
    prescriptions_db.prescriptions.pop(prescription_id)

