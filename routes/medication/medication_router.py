from fastapi import APIRouter
from . import add_medication

router = APIRouter()

router.include_router(add_medication.router)
