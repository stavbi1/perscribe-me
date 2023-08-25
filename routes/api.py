from fastapi import APIRouter
from routes.prescription.prescription_router import router as prescription_router
from routes.medication.medication_router import router as medication_router

router = APIRouter()

router.include_router(prescription_router, prefix="/prescription")
router.include_router(medication_router, prefix="/medication")
