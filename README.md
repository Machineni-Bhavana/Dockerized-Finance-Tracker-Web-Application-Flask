# 💰 Dockerized Finance Tracker Web Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-green?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Containerization-Docker-blue?logo=docker&logoColor=white)
![Database](https://img.shields.io/badge/Database-SQLite%2FSQLAlchemy-lightgrey?logo=sqlite&logoColor=white)

A full-stack, containerized web application built with **Python**, **Flask**, **SQLAlchemy**, and **Docker** designed to help users track personal incomes, expenses, categories, and real-time net balances through an intuitive, user-friendly interface.

---

## 📌 Project Overview

The **Dockerized Finance Tracker** provides an efficient solution for personal expense tracking and financial budgeting. Built following Flask best practices—including the **Application Factory pattern** (`create_app`), modular **Blueprints** (`auth`, `finance`, `routes`), and **SQLAlchemy ORM**—the application ensures scalable backend management and containerized deployment across any environment using **Docker**.

### 🎯 Key Objectives
* **Transaction Logging**: Record income and expense entries with custom categories, dates, and descriptions.
* **Financial Analytics**: Dynamically calculate and display Total Income, Total Expenses, and Net Balance.
* **Modular Architecture**: Utilize Flask Blueprints and factory patterns for clean separation of concerns.
* **Docker Containerization**: Provide single-command environment initialization using Docker container specifications.
* **Version Control**: Demonstrate production-level Git & GitHub workflow standards.

---

## 🛠️ Technology Stack

* **Backend Framework**: Python 3.10+, Flask
* **Database & ORM**: SQLite, Flask-SQLAlchemy
* **Frontend**: HTML5, CSS3, Jinja2 Templating
* **Containerization**: Docker, Docker Compose
* **Version Control**: Git, GitHub

---

## ⚙️ Core Features

- 🔒 **User Authentication & Session Management**: Register, log in, and securely manage user sessions.
- 💵 **Income & Expense Tracking**: Add income sources and expense items with customizable categories.
- 📊 **Real-time Balance Summaries**: Instant dashboard updates for Total Income, Total Expenses, and Net Savings.
- 📜 **Transaction History**: Filterable and organized table view of all historical financial records.
- 🐳 **Docker Readiness**: Pre-configured Dockerfile for containerized deployment across development and production environments.

---

## 📂 Project Structure
## 📂 Project Structure

```text
Dockerized-Finance-Tracker-Web-Application-Flask/
│
├── app/
│   ├── __init__.py              # Application factory and Flask configuration
│   ├── models.py                # SQLAlchemy models (User, Transaction, Category)
│   │
│   ├── routes/
│   │   ├── __init__.py          # Routes package initialization
│   │   ├── auth.py              # Authentication routes (register, login, logout)
│   │   ├── finance.py           # Transaction management and finance routes
│   │   └── main.py              # Dashboard and homepage routes
│   │
│   ├── static/
│   │   ├── css/                 # CSS stylesheets
│   │   ├── js/                  # JavaScript files
│   │   └── images/              # Application images and assets
│   │
│   └── templates/
│       ├── base.html             # Base Jinja2 template
│       ├── dashboard.html        # Financial dashboard
│       ├── login.html            # User login page
│       ├── register.html         # User registration page
│       └── transactions.html     # Transaction management page
│
├── run.py                        # Application entry point
├── Dockerfile                    # Docker container configuration
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git exclusion rules
└── README.md                     # Project documentation
```



---
## 🚀 Quick Start Guide
### Option 1: Run Locally with Python Virtual Environment
#### 1. Clone the Repository
```bash
git clone https://github.com/Machineni-Bhavana/Dockerized-Finance-Tracker-Web-Application-Flask.git
cd Dockerized-Finance-Tracker-Web-Application-Flask
2. Create and Activate a Virtual Environment
bash


# On macOS / Linux
python3 -m venv venv
source venv/bin/activate
# On Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash


pip install -r requirements.txt
4. Run the Flask Development Server
bash


python run.py
Open your web browser and navigate to http://127.0.0.1:5000.

Option 2: Run with Docker 🐳
1. Build the Docker Image
bash


docker build -t finance-tracker-app .
2. Run the Docker Container
bash


docker run -p 5000:5000 finance-tracker-app
Access the application at http://localhost:5000.

🌐 API & Application Routes
Route	HTTP Method	Description
/	GET	Main Dashboard Summary (Total Income, Expenses, Net Balance)
/auth/register	GET, POST	User Registration Form & Account Creation
/auth/login	GET, POST	User Authentication & Session Login
/auth/logout	GET	User Logout & Session Invalidation
/finance/add	GET, POST	Record New Income / Expense Entry
/finance/history	GET	View Historical Transaction Logs
🎓 Technical Interview Defensibility Guide
1. Why use the Flask Application Factory pattern (create_app)?
Answer: The Application Factory pattern creates app instances dynamically inside a function. This prevents global state mutation, allows multiple app instances with distinct configurations (Development, Testing, Production), and avoids circular import issues.

2. How are Flask Blueprints structured in this application?
Answer: Blueprints partition the application into modular components (e.g. auth for authentication, finance for transaction logic). Each blueprint encapsulates its own routes, views, and templates, ensuring high cohesion and code maintainability.

3. How does SQLAlchemy ORM manage database entities?
Answer: SQLAlchemy maps Python classes to relational database tables (e.g., User and Transaction models). It translates object-oriented Python code into optimized SQL queries, preventing SQL injection vulnerabilities.

4. How is Docker used to containerize this Flask application?
Answer: A custom Dockerfile specifies a lightweight Python base image (python:3.10-slim), copies dependencies (requirements.txt), installs packages, exposes port 5000, and executes python run.py (or Gunicorn) inside an isolated container environment.




