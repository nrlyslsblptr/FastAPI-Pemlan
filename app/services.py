
from app.repositories import InMemoryRepository
from app.schemas import (
    MedicationCreate,
    MedicationResponse,
    DoseLogCreate,
    DoseLogResponse,
    HealthEntryCreate,
    HealthEntryResponse,
)


class MediTrackService:
    def __init__(self, repo: InMemoryRepository):
        self.repo = repo

    def create_medication(
        self, payload: MedicationCreate
    ) -> MedicationResponse:
        item = MedicationResponse(
            id=self.repo.next_id("medication"),
            **payload.model_dump(),
        )
        self.repo.medications[item.id] = item
        return item

    def list_medications(self):
        return list(self.repo.medications.values())

    def create_dose_log(
        self, payload: DoseLogCreate
    ) -> DoseLogResponse | None:
        if payload.medication_id not in self.repo.medications:
            return None

        item = DoseLogResponse(
            id=self.repo.next_id("dose_log"),
            **payload.model_dump(),
        )
        self.repo.dose_logs[item.id] = item
        return item

    def list_dose_logs(self):
        return list(self.repo.dose_logs.values())

    def create_health_entry(
        self, payload: HealthEntryCreate
    ) -> HealthEntryResponse:
        item = HealthEntryResponse(
            id=self.repo.next_id("health_entry"),
            **payload.model_dump(),
        )
        self.repo.health_entries[item.id] = item
        return item

    def list_health_entries(self):
        return list(self.repo.health_entries.values())
