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
