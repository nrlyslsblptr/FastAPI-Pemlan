
from fastapi.testclient import TestClient

from app.main import app
from app.repositories import repository

client = TestClient(app)


def setup_function():
    repository.medications.clear()
    repository.dose_logs.clear()
    repository.health_entries.clear()
    repository._next_ids = {
        "medication": 1,
        "dose_log": 1,
        "health_entry": 1,
    }


def medication_payload():
    return {
        "medication_name": "Contoh obat A",
        "scheduled_date": "2026-11-01",
        "scheduled_time": "08:00:00",
        "instructions": "Data simulasi",
    }


def test_create_medication():
    response = client.post(
        "/api/v1/medication-schedules",
        json=medication_payload(),
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["medication_name"] == "Contoh obat A"


def test_reject_invalid_medication():
    payload = medication_payload()
    payload["medication_name"] = ""

    response = client.post(
        "/api/v1/medication-schedules",
        json=payload,
    )

    assert response.status_code == 422


def test_create_dose_log():
    client.post(
        "/api/v1/medication-schedules",
        json=medication_payload(),
    )

    response = client.post(
        "/api/v1/dose-logs",
        json={
            "medication_id": 1,
            "log_date": "2026-11-01",
            "status": "taken",
            "notes": "Data simulasi",
        },
    )

    assert response.status_code == 201
    assert response.json()["status"] == "taken"


def test_dose_log_requires_existing_medication():
    response = client.post(
        "/api/v1/dose-logs",
        json={
            "medication_id": 999,
            "log_date": "2026-11-01",
            "status": "taken",
            "notes": None,
        },
    )

    assert response.status_code == 404


def test_reject_invalid_dose_status():
    client.post(
        "/api/v1/medication-schedules",
        json=medication_payload(),
    )

    response = client.post(
        "/api/v1/dose-logs",
        json={
            "medication_id": 1,
            "log_date": "2026-11-01",
            "status": "maybe",
            "notes": None,
        },
    )

    assert response.status_code == 422


def test_create_health_entry():
    response = client.post(
        "/api/v1/health-entries",
        json={
            "entry_date": "2026-11-01",
            "general_notes": "Contoh catatan harian",
            "mood": "baik",
        },
    )

    assert response.status_code == 201
    assert response.json()["general_notes"] == "Contoh catatan harian"


def test_list_medications():
    client.post(
        "/api/v1/medication-schedules",
        json=medication_payload(),
    )

    response = client.get("/api/v1/medication-schedules")

    assert response.status_code == 200
    assert len(response.json()) == 1
