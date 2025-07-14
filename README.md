# Kpa_project
# KPA Form Data Backend

A Django REST Framework (DRF) application implementing two KPA Form Data APIs: bogie checksheet submission and wheel specifications retrieval/submission. This project demonstrates JSONField usage, DRF serializers/views, PostgreSQL integration, and a clean URL structure.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Postman Collection](#postman-collection)
- [Project Structure](#project-structure)

## Project Overview
This backend provides two primary endpoints under `/api/forms/`:

1. **POST /api/forms/bogie-checksheet**  
   Submit a bogie inspection form. Accepts nested JSON for checksheets and details; returns a confirmation with form number and status.

2. **GET, POST /api/forms/wheel-specifications**  
   - GET: Retrieve saved wheel-specification forms, with optional filters `formNumber`, `submittedBy`, and `submittedDate`.  
   - POST: Submit a new wheel-specification form with a JSON body; returns confirmation and form metadata.

Both endpoints adhere exactly to the provided Postman/Swagger JSON schema.

## Tech Stack
- Python 3.x  
- Django 5.x  
- Django REST Framework  
- PostgreSQL  
- python-decouple (for `.env` management)

## Prerequisites
- Python 3.8+  
- PostgreSQL 12+  
- Git  
- (Optional) Virtual environment tool (venv)

## Installation & Setup
1. Clone the repository  
    git clone https://github.com/YourUser/Kpa_project.git  
    cd Kpa_project

2. Create and activate a virtual environment  
    python3 -m venv env  
    source env/bin/activate      # Windows: env\Scripts\activate

3. Install dependencies  
    pip install -r requirements.txt

## Configuration
1. Environment variables  
   Copy `.env.example` to `.env` and set:
       DB_NAME=kpa_db  
       DB_USER=kpa_user  
       DB_PASSWORD=kpa_pass  
       DB_HOST=localhost  
       DB_PORT=5432  
       SECRET_KEY=your_django_secret_key  
       DEBUG=True  
2. Add `.env` to `.gitignore`

## Database Setup
1. Create PostgreSQL database and user  
       CREATE DATABASE kpa_db;  
       CREATE USER kpa_user WITH PASSWORD 'kpa_pass';  
       GRANT ALL PRIVILEGES ON DATABASE kpa_db TO kpa_user;  
2. Apply Django migrations  
       python manage.py migrate

## Running the Server
Start the development server:  
    python manage.py runserver  
The API is at http://127.0.0.1:8000/

## API Endpoints
All routes are prefixed with `/api/forms/`.

### 1. Bogie Checksheet
**POST** `/api/forms/bogie-checksheet`  
Request Body (JSON):
    {
      "formNumber": "BOGIE-2025-001",
      "inspectionBy": "user_id_456",
      "inspectionDate": "2025-07-03",
      "bmbcChecksheet": { ... },
      "bogieChecksheet": { ... },
      "bogieDetails": { ... }
    }  
Response (201 Created):
    {
      "success": true,
      "message": "Bogie checksheet submitted successfully.",
      "data": {
        "formNumber": "BOGIE-2025-001",
        "inspectionBy": "user_id_456",
        "inspectionDate": "2025-07-03",
        "status": "Saved"
      }
    }

### 2. Wheel Specifications
**GET** `/api/forms/wheel-specifications`  
Optional Query Params: `formNumber`, `submittedBy`, `submittedDate`  
Response (200 OK):
    {
      "success": true,
      "message": "Wheel specifications fetched successfully.",
      "data": [ { /* form objects */ } ]
    }

**POST** `/api/forms/wheel-specifications`  
Request Body (JSON):
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": { /* measurement fields */ }
    }  
Response (201 Created):
    {
      "success": true,
      "message": "Wheel specification submitted successfully.",
      "data": {
        "formNumber": "WHEEL-2025-001",
        "status": "Saved",
        "submittedBy": "user_id_123",
        "submittedDate": "2025-07-03"
      }
    }

## Postman Collection
Import `postman_collection/KPA_FormData.postman_collection.json` to test endpoints.

## Project Structure
Kpa_project/  
├── forms_app/  
│   ├── migrations/  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── models.py  
│   ├── serializers.py  
│   ├── urls.py  
│   ├── views.py  
│   └── tests.py  
├── kpa_project/  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── .env.example  
├── manage.py  
├── requirements.txt  
└── postman_collection/  
    └── KPA_FormData.postman_collection.json
*
