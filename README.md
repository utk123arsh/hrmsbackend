# HRMS Lite – Backend

📌 **Lightweight Human Resource Management System** – REST API for employee management and attendance tracking.

## 🛠 Tech Stack

- **Python 3.13** + Django 6.0
- **Django REST Framework** (DRF)
- **PostgreSQL** (Docker)
- **Docker & Docker Compose**
- **Gunicorn** (Production WSGI)
- **SQLite** (Local development)

## ✨ Features

✅ Employee Management (Create, List, Delete)  
✅ Attendance Tracking (Mark, View, Filter)  
✅ Prevent duplicate attendance (same employee + date)  
✅ Weekend validation (no attendance marking)  
✅ Email validation  
✅ Unique employee IDs  
✅ Proper HTTP status codes  
✅ RESTful API with DefaultRouter  
✅ CORS enabled for frontend  
✅ Public API (no authentication)  

## 📂 Project Structure

```
hrms-backend/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Procfile
├── README.md
├── .gitignore
├── hrms/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── core/
    ├── models.py      # Employee, Attendance
    ├── serializers.py # Serialization logic
    ├── views.py       # ViewSets
    ├── urls.py        # API Routes
    └── migrations/
```

## 🚀 Quick Start (Local)

### Using Docker Compose

```bash
cd hrms-backend
docker-compose up --build
```

- **API**: http://localhost:8000/api/
- **Admin**: http://localhost:8000/admin/ (admin:admin123)
- **Database**: PostgreSQL on port 5432

### Without Docker (SQLite)

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- **API**: http://127.0.0.1:8000/api/

## 📡 API Endpoints

### Employees

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees/` | List all employees |
| POST | `/api/employees/` | Create employee |
| GET | `/api/employees/{id}/` | Get employee |
| PUT | `/api/employees/{id}/` | Update employee |
| DELETE | `/api/employees/{id}/` | Delete employee |

### Attendance

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/attendance/` | List all attendance |
| POST | `/api/attendance/` | Mark attendance |
| GET | `/api/attendance/{id}/` | Get attendance record |
| PUT | `/api/attendance/{id}/` | Update attendance |
| DELETE | `/api/attendance/{id}/` | Delete attendance |

## 📝 Example Requests

### Add Employee

```bash
curl -X POST http://localhost:8000/api/employees/ \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "EMP001",
    "full_name": "John Doe",
    "email": "john@example.com",
    "department": "IT"
  }'
```

### Mark Attendance

```bash
curl -X POST http://localhost:8000/api/attendance/ \
  -H "Content-Type: application/json" \
  -d '{
    "employee": 1,
    "date": "2026-02-25",
    "status": "Present"
  }'
```

## 🌐 Deployment (Railway)

Backend hosted at: **https://splendid-wholeness-production-ecb0.up.railway.app**

### Deploy Your Own

```bash
# Push to GitHub
git add .
git commit -m "Initial HRMS backend setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hrmsbackend.git
git push -u origin main

# Then connect to Railway
# 1. Go to railway.app
# 2. New Project → Deploy from GitHub
# 3. Select your hrmsbackend repo
# 4. Add PostgreSQL service
# 5. Done! ✅
```

## 📋 Database Models

### Employee
- `employee_id` (unique)
- `full_name`
- `email` (unique)
- `department`

### Attendance
- `employee` (FK to Employee)
- `date`
- `status` (Present/Absent)
- `unique_together` (employee, date)

## ✅ Validation

- ❌ No attendance on weekends
- ❌ No duplicate attendance (same employee + date)
- ✅ Valid email required
- ✅ Unique employee IDs
- ✅ Proper HTTP status codes

## 📦 Requirements

See `requirements.txt`:
- Django 6.0.2
- djangorestframework 3.16.1
- django-cors-headers 4.9.0
- psycopg2-binary 2.9.11
- gunicorn 23.0.0
- dj-database-url 3.1.2

## 🔧 Environment Variables (Railway)

```
DEBUG=False
ALLOWED_HOSTS=your-app.up.railway.app
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
```

## 📝 Notes

- Single admin user (no multi-role system)
- No authentication required (public API)
- Leave & payroll features out of scope
- Soft delete not implemented

## 🚀 Ready to Deploy!

This backend is production-ready and can be deployed to:
- ✅ Railway
- ✅ Heroku
- ✅ AWS
- ✅ Any Docker-compatible platform

Connect your React frontend to get started! 🎨
