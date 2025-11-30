Task Prioritizer — Django + REST API

A smart task-management tool where users can paste task JSON, analyze priorities, save tasks to the database, export CSV, and manage authentication (login/register).
Built with Django 5, Django REST Framework, and a simple responsive UI.

🚀 Features
🔹 Core Features

Paste JSON tasks and analyze them instantly

Save tasks to database

Load saved tasks

Export saved tasks as CSV

Strategy selection:

Smart Balance

Fastest Wins

High Impact

Deadline Driven

🔹 Authentication

User Register

User Login

User Profile

Admin panel (/admin/) for managing tasks & users

🔹 API Endpoints
Endpoint	Method	Description
/api/tasks/saved/	GET	Load saved tasks
/api/tasks/saved/	POST	Save new tasks
/api/tasks/saved/export/	GET	Export tasks to CSV
📂 Project Structure
task-prioritizer/
│
├── accounts/          # Login, Register
├── tasks/             # Task model, views, API
├── backend/           # Main Django settings & URLs
├── templates/         # HTML templates
├── static/            # CSS, JS
│
├── db.sqlite3
├── manage.py
└── requirements.txt

⚙️ Installation & Setup (Local Machine)
1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/TASK-PRIORITIZER.git
cd TASK-PRIORITIZER

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Apply Migrations
python manage.py migrate

6️⃣ Create Superuser (for Admin Access)
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver


Visit:

🌐 Home: http://127.0.0.1:8000

🔐 Login: http://127.0.0.1:8000/accounts/login/

🛠 Admin: http://127.0.0.1:8000/admin/

📸 Screenshots

Add screenshots of your UI here when ready.

📦 API Usage Example
Save JSON → DB
POST /api/tasks/saved/

[
  {
    "id": "t1",
    "title": "Build Feature",
    "due_date": "2025-12-01",
    "estimated_hours": 3,
    "importance": 8,
    "dependencies": []
  }
]

Load Saved Tasks
GET /api/tasks/saved/

Export CSV
GET /api/tasks/saved/export/

🧩 Tech Stack

Backend: Django 5, Django REST Framework

Frontend: HTML, CSS, JS

Database: SQLite (default)

Auth: Django Auth System

Export: CSV Writer

API: DRF Class-Based Views

📱 Responsive UI

Mobile-friendly layout

Flexbox button groups

Scalable textarea + inputs

Midnight theme included

🧑‍💻 Development Commands
Create app
python manage.py startapp accounts
python manage.py startapp tasks

Collect static files (production)
python manage.py collectstatic
