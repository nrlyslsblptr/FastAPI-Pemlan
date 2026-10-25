
from fastapi import APIRouter, HTTPException, status

from app.repositories import repository
from app.services import MediTrackService
from app.schemas import (
    MedicationCreate,
    MedicationResponse,
    DoseLogCreate,
    DoseLogResponse,
    HealthEntryCreate,
    HealthEntryResponse,
)

router = APIRouter(prefix="/api/v1", tags=["MediTrack"])
service = MediTrackService(repository)


@router.post(
    "/medication-schedules",
    response_model=MedicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_medication(payload: MedicationCreate):
    return service.create_medication(payload)


@router.get(
    "/medication-schedules",
    response_model=list[MedicationResponse],
)
def list_medications():
    return service.list_medications()


@router.post(
    "/dose-logs",
    response_model=DoseLogResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dose_log(payload: DoseLogCreate):
    result = service.create_dose_log(payload)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Medication schedule not found",
        )

    return result


@router.get(
    "/dose-logs",
    response_model=list[DoseLogResponse],
)
def list_dose_logs():
    return service.list_dose_logs()


@router.post(
    "/health-entries",
    response_model=HealthEntryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_health_entry(payload: HealthEntryCreate):
    return service.create_health_entry(payload)


@router.get(
    "/health-entries",
    response_model=list[HealthEntryResponse],
)
def list_health_entries():
    return service.list_health_entries()
