from fastapi import APIRouter
from . import open_prescription
from . import close_prescription

router = APIRouter()

router.include_router(open_prescription.router)
router.include_router(close_prescription.router)
