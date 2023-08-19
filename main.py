from fastapi import FastAPI
from routes.prescription.prescription_router import router as prescription_router
from routes.medication.medication_router import router as medication_router

app = FastAPI()

app.include_router(prescription_router, prefix="/prescription")
app.include_router(medication_router, prefix="/medication")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
