
from datetime import date, time
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class DoseStatus(str, Enum):
    TAKEN = "taken"
    SKIPPED = "skipped"


class MedicationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    medication_name: str = Field(min_length=2, max_length=100)
    scheduled_date: date
    scheduled_time: time
    instructions: str | None = Field(default=None, max_length=200)


class MedicationResponse(MedicationCreate):
    id: int


class DoseLogCreate(BaseModel):
    medication_id: int = Field(gt=0)
    log_date: date
    status: DoseStatus
    notes: str | None = Field(default=None, max_length=200)


class DoseLogResponse(DoseLogCreate):
    id: int


class HealthEntryCreate(BaseModel):
    entry_date: date
    general_notes: str = Field(min_length=1, max_length=500)
    mood: str | None = Field(default=None, max_length=30)


class HealthEntryResponse(HealthEntryCreate):
    id: int
