
# MediTrack API

Backend REST API untuk pencatatan jadwal obat dan catatan kesehatan harian menggunakan FastAPI.

## Teknologi
- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX
- Uvicorn

## Fitur
- Membuat dan melihat jadwal obat
- Mencatat status jadwal
- Membuat dan melihat catatan kesehatan
- Validasi data request dan response
- Unit testing

## Instalasi

```bash
python -m venv .venv
```

Aktifkan virtual environment, kemudian jalankan:

```bash
pip install -r requirements.txt
```

## Menjalankan server

```bash
uvicorn app.main:app --reload
```

Dokumentasi API tersedia di:
http://127.0.0.1:8000/docs

## Menjalankan unit test

```bash
python -m pytest -v
```

## Penyimpanan

Data disimpan sementara di memori dan akan hilang
ketika aplikasi dimulai ulang.

## Batasan

API merupakan sarana pencatatan, bukan alat diagnosis
atau pemberi rekomendasi pengobatan.
