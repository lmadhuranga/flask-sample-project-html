# Flask User Management Application

A Flask-based User Management application demonstrating **REST API development and server-rendered HTML CRUD operations** using Flask, SQLAlchemy, SQLite, Marshmallow, Flasgger, and pytest.

The project is designed as a learning project that demonstrates a clean separation between:

* Routes
* Services
* Models
* Schemas
* HTML templates
* REST APIs
* Tests

---

## Features

### REST API

* Get all users
* Get user by ID
* Create user
* Update user
* Delete user
* JSON responses
* Request validation
* Duplicate email handling
* HTTP status codes
* Swagger API documentation

### HTML Web Application

* Display users
* Create user
* Edit user
* Delete user
* Form validation
* Flash messages
* Jinja2 templates
* CSS styling
* Confirmation before deleting a user

### Database

* SQLite
* SQLAlchemy ORM
* User model
* Unique email constraint

### Testing

* pytest
* Flask test client
* In-memory SQLite database for tests
* REST API tests
* HTML route tests

---

## Project Architecture

```text
                    Browser
                       |
                       v
                +--------------+
                | Flask Routes |
                +------+-------+
                       |
             +---------+---------+
             |                   |
             v                   v
       REST API Routes      HTML Routes
             |                   |
             |                   v
             |              Jinja Templates
             |                   |
             +---------+---------+
                       |
                       v
                +--------------+
                | User Service |
                +------+-------+
                       |
                       v
                +--------------+
                | User Schema  |
                +------+-------+
                       |
                       v
                +--------------+
                | User Model   |
                +------+-------+
                       |
                       v
                    SQLite
```

---

## Project Structure

```text
flask-user-app/
│
├── app.py
├── extensions.py
├── requirements.txt
├── README.md
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
│   ├── user_routes.py
│   └── web_routes.py
│
├── templates/
│   ├── base.html
│   │
│   └── users/
│       ├── list.html
│       ├── create.html
│       └── edit.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
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

# Requirements

* Python 3.10+
* Flask
* Flask-SQLAlchemy
* Flask-Marshmallow
* Marshmallow
* Flasgger
* pytest

---

# Installation

## 1. Clone the project

```bash
git clone <repository-url>
cd flask-user-app
```

## 2. Create a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

Start Flask:

```bash
flask --app app run --debug
```

Or:

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

---

# HTML Web Application

Open:

```text
http://127.0.0.1:5000/users
```

You will see the User Management interface.

## User List

The user list provides:

* User ID
* Name
* Email
* Edit button
* Delete button
* Add User button

Example:

```text
+------------------------------------------------------+
| Users                                  [Add User]    |
+------------------------------------------------------+
| ID | Name          | Email             | Actions     |
+----+---------------+-------------------+-------------+
| 1  | John          | john@example.com  | Edit Delete  |
| 2  | David         | david@example.com | Edit Delete  |
+----+---------------+-------------------+-------------+
```

---

# HTML Routes

| Method | URL                  | Description         |
| ------ | -------------------- | ------------------- |
| GET    | `/users`             | Display all users   |
| GET    | `/users/create`      | Display create form |
| POST   | `/users/create`      | Create user         |
| GET    | `/users/<id>/edit`   | Display edit form   |
| POST   | `/users/<id>/edit`   | Update user         |
| POST   | `/users/<id>/delete` | Delete user         |

---

# Creating a User

Open:

```text
http://127.0.0.1:5000/users/create
```

Enter:

```text
Name: John
Email: john@example.com
```

Click:

```text
Create User
```

The application will:

```text
HTML Form
    ↓
Web Route
    ↓
User Service
    ↓
User Model
    ↓
SQLite
```

After successful creation, the user is redirected to:

```text
/users
```

---

# Editing a User

From the user list, click:

```text
Edit
```

The application opens:

```text
/users/<id>/edit
```

For example:

```text
/users/1/edit
```

The existing user information is displayed:

```text
Name:
[John]

Email:
[john@example.com]

[Update User] [Cancel]
```

After updating:

```text
Edit Form
    ↓
Web Route
    ↓
User Service
    ↓
User Model
    ↓
SQLite
```

---

# Deleting a User

Click:

```text
Delete
```

The browser asks for confirmation:

```text
Are you sure you want to delete this user?
```

If confirmed:

```text
POST /users/<id>/delete
```

The user is removed from the database.

A success message is displayed:

```text
User deleted successfully.
```

---

# REST API

The application also provides a REST API.

## Get All Users

```http
GET /users
```

Example:

```bash
curl http://127.0.0.1:5000/users
```

Response:

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
GET /users/<id>
```

Example:

```bash
curl http://127.0.0.1:5000/users/1
```

Response:

```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```

---

## Create User

```http
POST /users
```

Example:

```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{
    "name": "John",
    "email": "john@example.com"
}'
```

Response:

```json
{
    "id": 1,
    "name": "John",
    "email": "john@example.com"
}
```

HTTP status:

```text
201 Created
```

---

## Update User

```http
PUT /users/<id>
```

Example:

```bash
curl -X PUT http://127.0.0.1:5000/users/1 \
-H "Content-Type: application/json" \
-d '{
    "name": "John Updated",
    "email": "john.updated@example.com"
}'
```

---

## Delete User

```http
DELETE /users/<id>
```

Example:

```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```

Response:

```json
{
    "message": "User deleted successfully"
}
```

---

# API Status Codes

| Status | Meaning               |
| ------ | --------------------- |
| 200    | Successful request    |
| 201    | User created          |
| 400    | Invalid request       |
| 404    | User not found        |
| 409    | Duplicate email       |
| 500    | Internal server error |

---

# User Model

The `User` model represents the database table.

```python
class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )
```

The model is responsible for the **database structure and persistence**.

```text
User Model
     ↓
SQLAlchemy
     ↓
SQLite
```

---

# User Schema

The `UserSchema` is responsible for **request validation and serialization/deserialization**.

Example:

```python
class UserSchema(Schema):

    name = fields.Str(
        required=True,
        validate=validate.Length(
            min=2,
            max=100
        )
    )

    email = fields.Email(
        required=True
    )
```

For example, this request:

```json
{
    "name": "J",
    "email": "invalid"
}
```

will fail validation.

---

# Model vs Schema

The project intentionally separates the database model from API validation.

| User Model               | User Schema            |
| ------------------------ | ---------------------- |
| Database layer           | API validation layer   |
| SQLAlchemy               | Marshmallow            |
| Defines database columns | Defines API data rules |
| Primary key              | Required fields        |
| Database constraints     | Email validation       |
| Relationships            | Length validation      |

Simple rule:

```text
Model  → How should the data be stored?

Schema → What data should the API accept/return?
```

---

# Service Layer

Business logic is placed inside:

```text
services/user_service.py
```

Example:

```python
class UserService:

    def create_user(self, name, email):
        ...
```

Routes should not contain database logic.

Instead:

```text
Route
  ↓
Service
  ↓
Model
  ↓
Database
```

This makes the application easier to:

* Test
* Maintain
* Extend
* Refactor

---

# Swagger API Documentation

Swagger documentation is available at:

```text
http://127.0.0.1:5000/apidocs/
```

Swagger provides an interactive interface for testing the REST API.

You can test:

```text
GET
POST
PUT
DELETE
```

directly from the browser.

---

# Testing

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Example:

```text
tests/
├── conftest.py
├── test_users_api.py
└── test_users_web.py
```

The tests use an in-memory SQLite database:

```text
sqlite:///:memory:
```

This prevents tests from modifying the development database.

---

# Testing REST API

Example:

```python
def test_create_user(client):

    response = client.post(
        "/users",
        json={
            "name": "John",
            "email": "john@example.com"
        }
    )

    assert response.status_code == 201
```

---

# Testing HTML

Example:

```python
def test_users_page(client):

    response = client.get("/users")

    assert response.status_code == 200
    assert b"Users" in response.data
```

---

# Database

The application uses SQLite.

The development database is automatically created when the application starts.

Example:

```text
users.db
```

Database table:

```text
users
-------------------------
id
name
email
```

The email column is unique:

```python
unique=True
```

Therefore duplicate emails are rejected.

---

# Flash Messages

The HTML application uses Flask flash messages.

Success:

```text
User created successfully.
```

Error:

```text
Email already exists.
```

The messages are displayed in the Jinja template using:

```python
get_flashed_messages()
```

---

# Configuration

For development, the application currently uses:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
```

For a production application, configuration should be moved to environment variables.

Example:

```text
DATABASE_URL
SECRET_KEY
FLASK_ENV
```

---

# Useful Commands

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Flask:

```bash
flask --app app run --debug
```

Run tests:

```bash
pytest
```

Run tests verbosely:

```bash
pytest -v
```

Check installed packages:

```bash
pip list
```

Generate requirements:

```bash
pip freeze > requirements.txt
```

---

# Learning Objectives

This project demonstrates the following Flask concepts:

* Flask application factory
* Blueprints
* REST APIs
* HTTP methods
* JSON responses
* Jinja2 templates
* HTML forms
* SQLAlchemy ORM
* SQLite
* Service layer
* Marshmallow schemas
* Input validation
* Error handling
* Flash messages
* Swagger/OpenAPI
* Unit testing
* Integration testing
* Application configuration
* Project structure
* Python docstrings

---

# Future Improvements

The application can be extended with:

1. JWT authentication
2. Password hashing
3. Login and logout
4. Role-based authorization
5. User registration
6. Pagination
7. Search and filtering
8. Sorting
9. Database migrations with Flask-Migrate
10. Environment-based configuration
11. Structured logging
12. Docker
13. CI/CD
14. PostgreSQL
15. Redis
16. Rate limiting
17. API versioning
18. Production deployment
19. Repository pattern
20. React/Next.js frontend

---

# Recommended Next Step

The next major feature should be **authentication**.

The application can evolve into:

```text
                    Flask Application
                           |
             +-------------+-------------+
             |                           |
          HTML App                    REST API
             |                           |
             +-------------+-------------+
                           |
                     Authentication
                           |
                    JWT / Password
                           |
                       UserService
                           |
                        User Model
                           |
                        Database
```

Authentication would introduce:

```text
POST /auth/register
POST /auth/login
POST /auth/logout
GET  /users
GET  /users/<id>
POST /users
PUT  /users/<id>
DELETE /users/<id>
```

with protected endpoints and authenticated users.

---

# License

This project is intended for learning and demonstration purposes.
