# Premium To-Do List Application

A high-performance, aesthetically pleasing To-Do List application built with **Django**, **Django REST Framework**, and **Vanilla JS**.

## ✨ Features
- **RESTful API**: Full CRUD operations for tasks.
- **Modern UI**: Clean, responsive, glassmorphism design.
- **Dynamic UX**: Real-time updates via Fetch API.
- **Logging & Error Handling**: Robust logging and custom error responses.
- **Automated Testing**: 100% API coverage using `pytest`.

---

## 🚀 Getting Started

### 1. Setup Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Run Application
```bash
python manage.py runserver
```

---

## 📡 API Documentation

### **Base URL**
`/api/tasks/`

### **Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/` | Retrieve all tasks |
| `POST` | `/api/tasks/` | Create a new task |
| `GET` | `/api/tasks/{id}/` | Retrieve a specific task |
| `PATCH` | `/api/tasks/{id}/` | Partially update a task |
| `DELETE` | `/api/tasks/{id}/` | Delete a task |

### **Request Body Schema (JSON)**
```json
{
  "title": "Task Title",
  "description": "Optional details",
  "due_date": "2023-10-31T23:59:00Z",
  "status": "Pending" | "Completed"
}
```

### **Response Format (Success)**
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Need organic milk",
  "due_date": "2023-10-31T23:59:00Z",
  "status": "Pending",
  "created_at": "...",
  "updated_at": "..."
}
```

---

## 🧪 Testing

Run all automated tests with:
```bash
pytest
```

---

## 🔐 Authentication
Currently, no authentication is implemented as per project requirements for open access. For production, **JWT** or **SessionAuth** is recommended.

---

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (Vanilla)
- **Database**: SQLite (Default)
- **Testing**: Pytest-django

---

## 👨‍💻 Submission Notes
- Git repository link: [TBD]
- Access: `hr@pelocal.com`
- Database: SQLite included (`db.sqlite3` will be created on migration)
