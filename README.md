**Dockerized Finance Tracker Web Application | Flask, Python, Docker**
**📌 Project Overview**

The Simple Finance Tracker Application is a web-based application built using Flask that helps users track their income and expenses in a structured and simple way.
The application allows users to add financial records, view summaries, and understand their spending patterns through a clean and user-friendly interface.

This project is designed to demonstrate practical usage of Python Flask, basic web technologies, and version control using Git.

**🎯 Objectives**

To build a simple finance tracking system using Flask

To allow users to record income and expenses

To display financial data in an organized manner

To understand backend–frontend integration using Flask

To practice Git and GitHub workflow

**🛠️ Technologies Used**

Python

Flask

HTML

CSS

SQLite (or in-memory storage, based on implementation)

Git & GitHub

**⚙️ Features**

Add income and expense records

Categorize transactions

View transaction history

Display total income, total expense, and balance

Simple and clean user interface

Lightweight and easy to run

**📂 Project Structure**
Finance_Tracker/
│
├── app/                     ← Core application package
│   ├── __init__.py           ← App factory (create_app)
│   ├── auth.py               ← Authentication logic (login/register)
│   ├── finance.py            ← Finance-related routes (expenses, dashboard)
│   ├── tasks.py              ← Task/utility-related routes
│   ├── models.py             ← Database models
│
│   ├── routes/               ← (Optional) route separation
│   │   └── __init__.py
│
│   ├── static/               ← Frontend static assets
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│
│   ├── templates/            ← HTML templates (Jinja2)
│   │   ├── base.html         ← Base layout
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   └── tasks.html
│
├── instance/                 ← Runtime configs (DB, secrets)
│
├── venv/                     ← Virtual environment (❌ should not be pushed)
│
├── run.py                    ← App entry point
├── Dockerfile                ← Container definition
├── requirements.txt          ← Python dependencies
├── .gitignore
└── sample.html               ← (Optional / can be removed)


**▶️ How to Run the Project
1️⃣ Clone the Repository**
git clone git@github.com:Machineni-Bhavana/Simple-Finance-tracker-application-using-flask.git

**2️⃣ Navigate to the Project Folder**
cd Simple-Finance-tracker-application-using-flask

**3️⃣ Create and Activate Virtual Environment**
python3 -m venv venv
source venv/bin/activate

**4️⃣ Install Dependencies**
pip install -r requirements.txt

**5️⃣ Run the Application**
python app.py

**6️⃣ Open in Browser**
http://127.0.0.1:5000/

**🧪 Sample Use Case**

User logs in

Adds income (salary, allowance, etc.)

Adds expenses (food, travel, shopping, etc.)

Views total income, total expense, and remaining balance

**📌 Future Enhancements**

User authentication with database storage

Monthly and yearly expense reports

Graphical visualization of expenses

Export data to CSV or PDF

Cloud deployment

**👩‍💻 Author**

Machineni Bhavana

**📜 License**

This project is created for academic and learning purposes.
