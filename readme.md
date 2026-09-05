# Flask User Management Application

A beginner-to-intermediate Flask application demonstrating how to build a **User Management system** using:

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Marshmallow
* Service Layer
* REST API
* HTML/Jinja CRUD
* Swagger/OpenAPI
* Pytest
* Test Coverage

The project is intentionally kept simple so that the Flask concepts are easy to understand before moving to more advanced architecture.

---

## Features

### REST API

* Get all users
* Get a user by ID
* Create a user
* Update a user
* Delete a user
* Request validation
* Duplicate email handling
* HTTP error handling

### HTML Web Application

* User list
* Create user
* Edit user
* Delete user
* Form validation
* Flash messages
* Jinja templates

### Database

* SQLite
* SQLAlchemy ORM
* Automatic table creation

### Validation

Marshmallow is used to validate API request data.

Example validation:

* Name is required
* Name must contain at least 2 characters
* Email is required
* Email must be a valid email address

### Testing

Pytest is used for automated testing.

Test coverage includes:

* API endpoints
* CRUD operations
* Validation
* Duplicate emails
* Not-found errors
* HTML pages
* Service layer

---

# Project Structure

```text
flask-user-app/
│
├── app.py
├── extensions.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── schemas/
│   ├── __init__.py
│   └── user_schema.py
│
├── services/
│   ├── __init__.py
│   └── user_service.py
│
├── routes/
│   ├── __init__.py
│   └── web_routes.py
│
├── templates/
│   ├── base.html
│   └── users/
│       ├── list.html
│       ├── create.html
│       └── edit.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_users_api.py
    └── test_users_web.py
```

---

# Architecture

The application follows a simple layered architecture:

```text
                Client
                  │
        ┌─────────┴─────────┐
        │                   │
     REST API            HTML/Jinja
        │                   │
        └─────────┬─────────┘
                  │
             web_routes.py
                  │
                  ▼
            UserSchema
                  │
                  ▼
           UserService
                  │
                  ▼
             SQLAlchemy
                  │
                  ▼
               SQLite
```

---

# Installation

## 1. Clone the project

```bash
git clone <repository-url>
cd flask-user-app
```

## 2. Create virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

## 3. Activate virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

# HTML Application

Open:

```text
http://127.0.0.1:5000/
```

The root URL redirects to:

```text
/users
```

## HTML Routes

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| GET    | `/`                  | Redirect to users |
| GET    | `/users`             | Display users     |
| GET    | `/users/create`      | Create-user form  |
| POST   | `/users/create`      | Create user       |
| GET    | `/users/<id>/edit`   | Edit-user form    |
| POST   | `/users/<id>/edit`   | Update user       |
| POST   | `/users/<id>/delete` | Delete user       |

---

# REST API

The REST API uses:

```text
/api/users
```

## Get All Users

```http
GET /api/users
```

Example response:

```json
[
    {
        "id": 1,
        "name": "John",
        "email": "john@example.com"
    }
]
```

---

## Get User

```http
GET /api/users/1
```

Example:

```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```

If the user doesn't exist:

```http
404 Not Found
```

```json
{
    "error": "User not found"
}
```

---

# Create User

```http
POST /api/users
```

Request:

```json
{
    "name": "John",
    "email": "john@example.com"
}
```

Response:

```http
201 Created
```

```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```

---

# Update User

```http
PUT /api/users/1
```

Request:

```json
{
    "name": "John Updated",
    "email": "john.updated@example.com"
}
```

Response:

```json
{
    "id": 1,
    "name": "John Updated",
    "email": "john.updated@example.com"
}
```

---

# Delete User

```http
DELETE /api/users/1
```

Response:

```json
{
    "message": "User deleted successfully"
}
```

---

# Validation

Marshmallow validates incoming API requests.

`schemas/user_schema.py`:

```python
from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    email = fields.Email(
        required=True
    )
```

Invalid request example:

```json
{
    "name": "J",
    "email": "invalid-email"
}
```

Response:

```http
400 Bad Request
```

---

# Service Layer

Business logic is kept inside:

```text
services/user_service.py
```

The service handles:

```text
create_user()
get_users()
get_user()
update_user()
delete_user()
```

The route should not directly perform database operations.

Instead:

```text
Route
  ↓
UserService
  ↓
User Model
  ↓
Database
```

This keeps the application easier to maintain and test.

---

# Database

The project uses SQLite:

```text
users.db
```

SQLAlchemy is used as the ORM.

User model:

```text
User
 ├── id
 ├── name
 └── email
```

The database tables are automatically created when the application starts.

The SQLite database is excluded from Git using `.gitignore`.

---

# Flask Secret Key

The application uses a Flask secret key because the HTML application uses `flash()` messages.

Example:

```python
app.config["SECRET_KEY"] = "dev-secret-key"
```

For production, the secret should be provided through an environment variable rather than hard-coded.

---

# Swagger API Documentation

Swagger is provided using Flasgger.

After starting the application, open:

```text
http://127.0.0.1:5000/apidocs/
```

Swagger provides an interactive interface for testing the REST API.

---

# Testing

Tests are written using Pytest.

Run all tests:

```bash
pytest
```

Example output:

```text
======================== test session starts ========================

tests/test_users_api.py ........
tests/test_users_web.py ........

========================= 16 passed ================================
```

---

# Test Coverage

Install coverage support:

```bash
pip install pytest-cov
```

Run tests with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

Example:

```text
Name                         Stmts   Miss  Cover
------------------------------------------------
app.py                          25      2    92%
models/user.py                 12      0   100%
routes/web_routes.py            45      2    96%
services/user_service.py        40      0   100%
schemas/user_schema.py          10      0   100%
------------------------------------------------
TOTAL                          132      4    97%
```

Generate an HTML coverage report:

```bash
pytest --cov=. --cov-report=html
```

Then open:

```text
htmlcov/index.html
```

---

# Recommended Coverage

The target for this project is:

```text
90%+
```

The most important code to cover is:

* Service logic
* API endpoints
* Validation
* Error handling
* CRUD operations

100% coverage is not required if some code is trivial or not meaningful to test.

---

# API Test Cases

The API tests cover:

### Users

```text
✓ Get users
✓ Create user
✓ Get user
✓ Get non-existing user
✓ Update user
✓ Update non-existing user
✓ Delete user
✓ Delete non-existing user
```

### Validation

```text
✓ Missing name
✓ Missing email
✓ Invalid email
✓ Invalid name
✓ Empty request
```

### Business Rules

```text
✓ Duplicate email
```

---

# HTTP Status Codes

| Status | Meaning                  |
| ------ | ------------------------ |
| 200    | Successful request       |
| 201    | Resource created         |
| 400    | Invalid request          |
| 404    | User not found           |
| 409    | Duplicate email/conflict |

---

# Useful Commands

Start application:

```bash
python app.py
```

Run tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=. --cov-report=term-missing
```

Generate HTML coverage:

```bash
pytest --cov=. --cov-report=html
```

Check Git status:

```bash
git status
```

---

# Git

The project contains a `.gitignore` file to exclude:

```text
.venv/
__pycache__/
*.pyc
users.db
.pytest_cache/
.coverage
htmlcov/
.env
.vscode/
.idea/
.DS_Store
```

---

# Learning Objectives

This project demonstrates the following Flask concepts:

* Flask application setup
* Application factory
* Blueprints
* REST APIs
* HTTP methods
* JSON requests/responses
* Jinja templates
* HTML forms
* Flash messages
* SQLAlchemy
* SQLite
* Service layer
* Marshmallow validation
* Error handling
* Swagger/OpenAPI
* Pytest
* Test coverage
* Git/GitHub project structure

---

# Current Architecture

The project intentionally keeps the architecture simple:

```text
Routes
   │
   ▼
Validation
   │
   ▼
Service
   │
   ▼
Model
   │
   ▼
SQLite
```

The REST API and HTML application are both handled through:

```text
routes/web_routes.py
```

The API uses:

```text
/api/users
```

while the HTML application uses:

```text
/users
```

This prevents the API from returning JSON when accessing the web application.

---

# Future Improvements

Possible next improvements:

* JWT authentication
* Password hashing
* User registration/login
* Role-based authorization
* Pagination
* Search/filtering
* Flask-Migrate
* PostgreSQL
* Docker
* CI/CD
* Redis
* Rate limiting
* API versioning
* React/Next.js frontend
* Better application configuration
* Production logging
* Structured error responses

Authentication is intentionally **not included yet** so the project can focus on understanding Flask CRUD, validation, service architecture, and testing first.

---

# Author

Flask User Management Learning Project

Built to understand Flask REST API and web application architecture step by step.
