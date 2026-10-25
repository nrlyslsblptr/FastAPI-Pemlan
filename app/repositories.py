
from app.schemas import (
    MedicationResponse,
    DoseLogResponse,
    HealthEntryResponse,
)


class InMemoryRepository:
    def __init__(self):
        self.medications: dict[int, MedicationResponse] = {}
        self.dose_logs: dict[int, DoseLogResponse] = {}
        self.health_entries: dict[int, HealthEntryResponse] = {}

        self._next_ids = {
            "medication": 1,
            "dose_log": 1,
            "health_entry": 1,
        }

    def next_id(self, resource: str) -> int:
        result = self._next_ids[resource]
        self._next_ids[resource] += 1
        return result


repository = InMemoryRepository()
