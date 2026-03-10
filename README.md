# FastAPI Backend – User Authentication & Profile Management

## Overview

This project implements a secure backend API using **FastAPI** and **MySQL**.
It includes authentication, JWT-based authorization, and CRUD operations for user profiles.

The system demonstrates secure backend development practices including password hashing, input validation, and token-based authentication.

---

## Features

* Secure **Signup and Login APIs**
* Password hashing using **bcrypt**
* **JWT Authentication** for protected endpoints
* **MySQL database integration**
* **User Profile CRUD operations**
* Input validation using **Pydantic**
* Domain-restricted email validation (`@nitp.ac.in` only)
* Organized backend architecture
* REST API documentation via **Swagger UI**

---

## Tech Stack

* **FastAPI**
* **Python**
* **MySQL**
* **SQLAlchemy**
* **Pydantic**
* **bcrypt**
* **JWT (python-jose)**

---

## Project Structure

```
backend/
│
├── main.py                # FastAPI entry point
├── database.py            # MySQL database connection
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic validation schemas
│
├── routes/
│   ├── auth_routes.py     # Signup and Login APIs
│   └── user_routes.py     # User profile APIs
│
├── utils/
│   ├── hashing.py         # Password hashing (bcrypt)
│   └── jwt_handler.py     # JWT token generation & verification
│
└── requirements.txt
```

---

## Installation

Clone the repository:

```
git clone https://github.com/meet9614/backend-nitp-api.git
cd backend-nitp-api
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Database Setup

Create MySQL database:

```
CREATE DATABASE faculty_db;
```

Update database connection in `database.py`:

```
DATABASE_URL = "mysql+pymysql://username:password@localhost/faculty_db"
```

---

## Running the Server

Start FastAPI server:

```
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

Interactive API documentation is automatically generated.

---

## API Endpoints

### Authentication

| Method | Endpoint  | Description       |
| ------ | --------- | ----------------- |
| POST   | `/signup` | Register new user |
| POST   | `/login`  | Authenticate user |

---

### User Profile

| Method | Endpoint                    | Description         |
| ------ | --------------------------- | ------------------- |
| PUT    | `/profile/update/{user_id}` | Update user profile |

---

## Security Features

* Password hashing using **bcrypt**
* **JWT-based authentication**
* **Input validation with Pydantic**
* Restricted email domain (`@nitp.ac.in`)
* Secure database interactions via SQLAlchemy

---

## Example Signup Request

```
POST /signup
```

```
{
"name": "Meet",
"email": "meet@nitp.ac.in",
"password": "securepassword"
}
```

---

## Author

**Meet Kumar Sarkar**
Data Science Student – NIT Patna
GitHub: https://github.com/meet9614
