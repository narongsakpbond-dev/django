# 5_rest_api (Django REST Framework)

## Requirements

- Python 3.x
- Windows PowerShell หรือ CMD

## Setup (Windows)

### 1) Create virtual environment

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependencies

```bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Database

โปรเจกต์ตั้งค่า DB เป็น `sqlite3` (ไฟล์ `db.sqlite3`) ใน `exam_app/settings.py`

### Run migrations

```bat
python manage.py migrate
```

### (Optional) Create admin user

สำหรับเข้า Django Admin และใช้ Session Login กับ Browsable API

```bat
python manage.py createsuperuser
```

## Run server

```bat
python manage.py runserver
```

จากนั้นเปิด:

- `http://127.0.0.1:8000/` (หน้า home)
- `http://127.0.0.1:8000/admin/` (Django Admin)

## API Documentation (Swagger / Redoc)

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- Redoc: `http://127.0.0.1:8000/api/redoc/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`

## API Base URL

- Base: `http://127.0.0.1:8000/api/v1/`

Resources ที่มี (จาก `apis/urls.py`):

- `schools`
- `classrooms`
- `teachers`
- `students`

ตัวอย่าง endpoints:

- `GET /api/v1/schools/`
- `POST /api/v1/schools/`
- `GET /api/v1/schools/{id}/`

(เช่นเดียวกันกับ `classrooms`, `teachers`, `students`)

=====END=====