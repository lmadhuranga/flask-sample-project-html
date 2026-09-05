# Flask User Management Application

A simple **Flask User Management application** built to learn and demonstrate Flask, Jinja2, SQLAlchemy, service-layer architecture, HTML CRUD operations, Bootstrap UI, pagination, testing, and code organization.

This project intentionally focuses on **server-rendered HTML pages** rather than a REST API.

---

## Features

* Flask web application
* Jinja2 templates
* Bootstrap 5 UI
* SQLAlchemy ORM
* SQLite database
* User CRUD operations

  * Create user
  * View users
  * Edit user
  * Delete user
* Server-side pagination
* Newest users displayed first
* Flash messages
* Email uniqueness validation
* Automatic fake user seeding
* Service layer
* Unit/integration tests with pytest
* Test coverage with pytest-cov
* Separate test database
* Responsive UI

---

## Technology Stack

| Technology       | Purpose              |
| ---------------- | -------------------- |
| Python           | Programming language |
| Flask            | Web framework        |
| Jinja2           | HTML templating      |
| Flask-SQLAlchemy | Database ORM         |
| SQLite           | Database             |
| Bootstrap 5      | UI framework         |
| pytest           | Testing              |
| pytest-cov       | Test coverage        |

---

## Project Architecture

The application follows a simple layered architecture:

```text
Browser
   │
   ▼
Flask Web Routes
   │
   ▼
User Service
   │
   ▼
SQLAlchemy Model
   │
   ▼
SQLite Database
```

### Responsibilities

**Routes**

Handle HTTP requests and render HTML pages.

**Service Layer**

Contains user-related business logic.

**Model**

Represents the database structure.

**Templates**

Render the HTML interface using Jinja2.

---

## Project Structure

```text
flask-users-oop-with-html/
│
├── app.py
├── extensions.py
├── seed.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── __init__.py
│   └── user.py
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
    └── test_users_web.py
```

---

# Installation

## 1. Clone the project

```bash
git clone <repository-url>
cd flask-users-oop-with-html
```

## 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

## 3. Activate the virtual environment

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

# Requirements

The project requires:

```text
Flask
Flask-SQLAlchemy
pytest
pytest-cov
```

Install them manually if required:

```bash
pip install Flask Flask-SQLAlchemy pytest pytest-cov
```

---

# Running the Application

Start the Flask application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open:

```text
http://127.0.0.1:5000/users
```

---

# Database

The application uses SQLite.

The database is created automatically when the application starts.

Example:

```text
users.db
```

The SQLAlchemy model is:

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

---

# Fake Users

When the application starts, it checks whether the database contains users.

If the database is empty, **15 fake users are automatically created**.

Example:

```text
John Smith
Sarah Johnson
Michael Brown
Emily Davis
David Wilson
Jessica Taylor
Daniel Anderson
Sophia Thomas
James Jackson
Olivia White
Robert Harris
Emma Martin
William Thompson
Ava Garcia
Christopher Martinez
```

The seed operation is designed to run only when there are no users.

Therefore restarting the application does not create duplicate users.

```text
Database empty
      │
      ▼
Create 15 fake users
      │
      ▼
Application starts
```

If users already exist:

```text
Database contains users
      │
      ▼
Skip seeding
```

---

# User CRUD

## List Users

```text
GET /users
```

Displays the user list.

The newest users are displayed first.

Users are sorted by:

```python
User.id.desc()
```

Example:

```text
ID    Name
-------------------------
15    Christopher Martinez
14    Ava Garcia
13    William Thompson
12    Emma Martin
...
```

---

## Create User

```text
GET  /users/create
POST /users/create
```

The create page contains:

* Name
* Email
* Create User button

Example:

```text
Name:
[ John Smith                 ]

Email:
[ john@example.com           ]

[ Create User ] [ Cancel ]
```

---

## Edit User

```text
GET  /users/<id>/edit
POST /users/<id>/edit
```

Example:

```text
/users/15/edit
```

The existing user information is displayed in the form.

---

## Delete User

```text
POST /users/<id>/delete
```

Users are deleted using a POST request.

A confirmation dialog is displayed before deletion.

---

# Pagination

The user list uses server-side pagination.

The current configuration displays:

```text
10 users per page
```

For example, with 15 users:

```text
Page 1
-------------------------
User 15
User 14
User 13
...
User 6

Page 2
-------------------------
User 5
User 4
User 3
User 2
User 1
```

Pagination URLs:

```text
/users?page=1
/users?page=2
```

The interface uses Bootstrap pagination components.

Example:

```text
[ Previous ] [ 1 ] [ 2 ] [ Next ]
```

The pagination buttons remain visible even when there is only one page.

Disabled buttons are displayed when there is no previous or next page.

---

# Bootstrap

The application uses Bootstrap 5 for the frontend UI.

Bootstrap is loaded through a CDN in:

```text
templates/base.html
```

Bootstrap is used for:

* Navbar
* Buttons
* Tables
* Forms
* Cards
* Alerts
* Pagination
* Responsive layout

This allows the project to focus on Flask and backend concepts without requiring a frontend framework.

---

# Flash Messages

The application uses Flask flash messages to display operation results.

Successful operations display messages such as:

```text
User created successfully.
```

```text
User updated successfully.
```

```text
User deleted successfully.
```

Validation errors display messages such as:

```text
Name and email are required.
```

```text
Email already exists.
```

Flash messages are displayed from the common:

```text
templates/base.html
```

This allows all pages to use the same notification system.

---

# Service Layer

User business logic is kept inside:

```text
services/user_service.py
```

Example:

```python
class UserService:

    def get_users(self, page=1, per_page=10):
        ...

    def get_user(self, user_id):
        ...

    def create_user(self, name, email):
        ...

    def update_user(self, user_id, name, email):
        ...

    def delete_user(self, user_id):
        ...
```

The routes do not directly contain database operations.

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

This makes the application easier to maintain and test.

---

# Testing

The project uses pytest.

Run all tests:

```bash
python -m pytest
```

Example:

```text
12 passed
```

The tests cover:

* User list
* User creation
* Duplicate email
* Missing name
* Missing email
* User editing
* Editing a non-existing user
* Duplicate email during update
* User deletion
* Deleting a non-existing user
* Pagination
* First page
* Second page
* Newest users appearing first

---

# Test Database

The application database and test database should be separated.

During normal development:

```text
SQLite
users.db
```

During tests:

```text
SQLite
in-memory database
```

This prevents test data from affecting the development database.

Tests should also **not use the 15 fake users**.

The fake users are development/demo data only.

The test database starts empty so each test can control its own data.

---

# Test Coverage

Install pytest-cov:

```bash
pip install pytest-cov
```

Run coverage:

```bash
python -m pytest --cov=. --cov-report=html
```

A coverage report will be generated in:

```text
htmlcov/
```

Open:

```text
htmlcov/index.html
```

You can also generate a terminal report:

```bash
python -m pytest --cov=. --cov-report=term-missing
```

---

# Example Test

Example user creation test:

```python
def test_create_user(client):

    response = client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"John Smith" in response.data
    assert b"john@example.com" in response.data
    assert b"User created successfully." in response.data
```

---

# Application Flow

Creating a user:

```text
Browser
   │
   │ POST /users/create
   ▼
web_routes.py
   │
   ▼
UserService.create_user()
   │
   ▼
User Model
   │
   ▼
SQLite
   │
   ▼
Commit
   │
   ▼
Flash message
   │
   ▼
Redirect /users
```

---

# Editing a User

```text
Browser
   │
   │ POST /users/15/edit
   ▼
web_routes.py
   │
   ▼
UserService.update_user()
   │
   ▼
User Model
   │
   ▼
SQLite
   │
   ▼
Redirect /users
```

---

# Deleting a User

```text
Browser
   │
   │ POST /users/15/delete
   ▼
web_routes.py
   │
   ▼
UserService.delete_user()
   │
   ▼
SQLite
   │
   ▼
Commit
   │
   ▼
Redirect /users
```

---

# Error Handling

The application handles common user errors.

### Duplicate email

Because email is unique:

```python
email = db.Column(
    db.String(150),
    unique=True,
    nullable=False
)
```

The service catches the database integrity error:

```python
try:
    db.session.commit()
except IntegrityError:
    db.session.rollback()
    return None
```

The route then displays:

```text
Email already exists.
```

---

# Current Scope

The current project intentionally contains:

* Flask
* Jinja2
* Bootstrap
* SQLAlchemy
* SQLite
* Service layer
* HTML CRUD
* Pagination
* Flash messages
* Automated fake data
* pytest
* Test coverage

The project **does not currently contain a REST API**.

REST API routes, Swagger/Flasgger, and API-specific tests have been removed to keep the project focused on server-rendered HTML CRUD.

---

# Learning Goals

This project is designed to help understand:

### Flask

* Application creation
* Routes
* Blueprints
* Request handling
* Redirects
* URL generation
* Flash messages
* Templates

### Jinja2

* Template inheritance
* Variables
* Loops
* Conditions
* `url_for()`
* Form rendering

### SQLAlchemy

* Models
* Columns
* Primary keys
* Unique constraints
* Queries
* Create
* Update
* Delete
* Transactions

### Architecture

* Routes
* Services
* Models
* Separation of concerns

### Testing

* pytest
* Flask test client
* Fixtures
* CRUD testing
* Pagination testing
* Test database
* Code coverage

### Frontend

* Bootstrap
* Forms
* Tables
* Cards
* Alerts
* Pagination
* Responsive layouts

---

# Future Improvements

Possible future improvements include:

* User authentication
* CSRF protection
* Better form validation
* Search users
* Sort users
* User detail page
* Database migrations with Flask-Migrate
* PostgreSQL
* Environment configuration
* Error handlers
* Logging
* Docker
* CI/CD
* Production configuration

These features can be added incrementally as the Flask concepts become familiar.

---

# Summary

This project provides a simple but structured example of a Flask application:

```text
Flask
  │
  ├── Web Routes
  │
  ├── Jinja2 Templates
  │
  ├── Bootstrap UI
  │
  ├── Service Layer
  │
  ├── SQLAlchemy
  │
  ├── SQLite
  │
  └── pytest
```

It is intentionally kept simple so that the core Flask concepts are easy to understand before introducing more advanced technologies such as authentication, REST APIs, microservices, Docker, or PostgreSQL.
