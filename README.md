# Django To-Do List Application

A robust, high-performance To-Do List application built using **Django**, **Django REST Framework**, and **Vanilla JavaScript**. This project demonstrates a full-stack CRUD implementation with a modern, responsive user interface.

## Features
- **RESTful API**: Full CRUD operations for task management.
- **Modern UI**: Clean design with responsive layouts for both desktop and mobile.
- **Dynamic UX**: Seamless task interaction using the Fetch API without page reloads.
- **Logging**: Integrated logging for request monitoring and error tracking.
- **Testing**: Automated API testing using `pytest`.

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- `pip`

### 2. Setup Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on Unix/macOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database & Static Files
```bash
# Apply migrations
python manage.py migrate
```

### 4. Running the Application
```bash
python manage.py runserver
```
Visit the app at: `http://127.0.0.1:8000/`

---

## API Documentation

### **Base URL**
`/api/tasks/`

### **Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/tasks/` | List all tasks |
| `POST` | `/api/tasks/` | Create a new task |
| `GET` | `/api/tasks/{id}/` | Get task details |
| `PATCH` | `/api/tasks/{id}/` | Update task status or details |
| `DELETE` | `/api/tasks/{id}/` | Delete a task |

### **Request Body (JSON)**
Example for creating/updating a task:
```json
{
  "title": "Build a great app",
  "description": "Complete the DRF integration",
  "due_date": "2023-10-31T23:59:00Z",
  "status": "Pending"
}
```

---

## Testing

Run the automated test suite with:
```bash
pytest
```

---

## Tech Stack
- **Backend**: Django & Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite3
- **Testing**: pytest-django

---

## Submission Notes
- **Repository**: [Premium_todo_app](https://github.com/Jitendrasha12/Premium_todo_app)
- **Reviewer Access**: Access has been granted to `hr@pelocal.com`.
- **Configuration**: The project includes a default `db.sqlite3` for ease of review.
