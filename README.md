

# FastAPI User Authentication

This is a simple FastAPI project that implements user registration and login functionality. It uses MongoDB for storing user data and bcrypt for password hashing.

## Features:
- **User Registration**: Allows users to register with their email and password.
- **User Login**: Allows users to log in by providing their email and password.
- **Password Hashing**: Passwords are securely hashed using bcrypt.
- **No JWT**: Login returns a simple success message instead of a token.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.7+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community) (Local or Atlas instance)
- [pip](https://pip.pypa.io/en/stable/)
## Screenshots



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

```bash
python -m venv venv
```

```bash
source venv\Scripts\activate
```


## Installation


### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Pavandollar/User-Authentication.git

```
  
### Step 2: Install the Dependencies

```bash
  pip install fastapi pymongo bcrypt uvicorn
```

### Step 3: configure MongoDB connection

- Make sure you have MongoDB running (either locally or use MongoDB Atlas).


### Step 4:  Run the FastAPI application

- Run the FastAPI server:

```bash
uvicorn main:app --reload
```




## Tech Stack

# Technologies Used

This project uses the following technologies:

## 1. **FastAPI** 
- **Version**: `0.95.0` (or latest)
- **Description**: FastAPI is a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It is known for its high performance and ease of use.
- **Link**: [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 2. **MongoDB Atlas**
- **Version**: `4.4` (or latest)
- **Description**: MongoDB is a NoSQL database that stores data in a flexible, JSON-like format. It is used in this project to store user data such as email and hashed passwords.
- **Link**: [MongoDB Official Website](https://www.mongodb.com/)



## 5. **Python**
- **Version**: `3.7+`
- **Description**: Python is the main programming language used to build the FastAPI application. This version ensures compatibility with all libraries and tools used in the project.
- **Link**: [Python Official Website](https://www.python.org/)

---

These are the core technologies used to develop the application, providing a solid foundation for building scalable and secure web APIs.




## Code Structure
- index.py: FastAPI application entry point.
- config/db.py: MongoDB connection configuration.
- models/user.py: User data model (Pydantic model).
- routes/user.py: User routes for registration, login, and password handling.
- requirements.txt: List of Python dependencies.


## Troubleshooting


- Error: "Password Hashing Failure": If you're getting an error related to password hashing, make sure you're using the correct hashing function (bcrypt in this case).
- Error: "MongoDB Connection Failure": Double-check your MongoDB connection string in the config/db.py file.
