# 🏅 Premium To-Do List Application (v1.1)

A professional, high-performance To-Do List manager built with **Django REST Framework** (Backend) and **Vanilla JS/CSS3** (Frontend).

---

## 🎨 Design Philosophy
This application follows **Premium Aesthetics** by incorporating:
- **Glassmorphism**: Semi-transparent UI elements with soft backdrop blurs.
- **Dynamic Feedback**: Real-time task sorting, status badges, and sleek micro-animations.
- **Responsive Layout**: Optimized for both desktop and mobile viewing with modern typography.

---

## 🚀 Environment Setup & Running

### 1. Prerequisites
- Python 3.10+
- `pip` (Python package manager)

### 2. Quick Installation
```bash
# 1. Clone the repository (if applicable)
# git clone <your-repo-url>
# cd crudOperation

# 2. Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt
```

### 3. Database Initialization
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Lauch Server
```bash
python manage.py runserver 0.0.0.0:8000
```
Visit the application at: **[http://localhost:8000/](http://localhost:8000/)**

---

## 📡 API Documentation

### **Authentication**
As per project requirements for open access, **No Authentication** is enforced for development. For production: **JWT (JSON Web Tokens)** or **Session-based Authentication** via Django Auth is proposed.

### **Base Endpoint**
`/api/tasks/`

### **Supported Endpoints**

| Method | Endpoint | Description | Expected Payload (JSON) |
|--------|----------|-------------|-------------------------|
| `GET` | `/api/tasks/` | Fetch all tasks | N/A |
| `POST` | `/api/tasks/` | Create a new task | `{ "title": "...", "due_date": "ISO-8601" }` |
| `GET` | `/api/tasks/{id}/` | Get task details | N/A |
| `PUT` | `/api/tasks/{id}/` | Full update (title, desc, etc.) | `{ "title": "New Title", ... }` |
| `PATCH` | `/api/tasks/{id}/` | Partial update (e.g., status) | `{ "status": "Completed" }` |
| `DELETE` | `/api/tasks/{id}/` | Delete a task | N/A |

### **Request/Response Formats**
Standard **JSON** is used for all communications.

**Example Task Object:**
```json
{
  "id": 1,
  "title": "Build premium UI",
  "description": "Utilize glassmorphism and modern CSS",
  "due_date": "2026-05-01T10:00:00Z",
  "status": "Pending",
  "created_at": "2026-04-03T14:00:00Z",
  "updated_at": "2026-04-03T14:00:00Z"
}
```

---

## 🧪 Testing & Quality Assurance

### **Automated Tests**
This project uses **Pytest** for backend API validation.
- **Coverage**: 100% of core CRUD operations.
- **How to execute**:
```bash
pytest
```

### **Deployment Considerations**
- **Production Server**: Use Gunicorn or uWSGI for production rather than the built-in development server.
- **Environment Variables**: Move `SECRET_KEY` and database credentials to a `.env` file.
- **CORS**: Currently configured for permissive access (`CORS_ALLOW_ALL_ORIGINS = True`). Restrict to specific domains in production.
- **Static Files**: Use `python manage.py collectstatic` for production serving.

---

## 👨‍💻 Submission Guidelines

1. **Repository**: Ensure this directory is initialized as a Git repository.
2. **Access**: Please grant repository access to **`hr@pelocal.com`**.
3. **Environment**: This codebase includes a `requirements.txt` and a default `sqlite3` database setup for immediate evaluation.
