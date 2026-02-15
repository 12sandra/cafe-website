# ☕ Cafe Website - Django Project

A full-stack Cafe Website built using Django.  
This project includes user registration, CRUD operations, and static cafe pages like menu, about, and contact.

---

## 🚀 Live Demo

Deployed on Railway:
https://mycafewebsite-f6d7.up.railway.app/


https://github.com/user-attachments/assets/178d2117-f47f-48bd-8da2-a7f38e3063fc

---

## 📌 Features

- 🏠 Home Page
- 📖 About Page
- 🍽️ Menu Page
- 📞 Contact Page
- 👤 User Registration
- 📋 View Users Table
- ✏️ Edit User
- 🗑️ Delete User
- 🗄️ PostgreSQL Database (Production)
- 📦 SQLite (Local Development)

---

## 🛠️ Tech Stack

- Python 3.13
- Django 6
- PostgreSQL
- Gunicorn
- WhiteNoise
- Railway Deployment

---

## 📂 Project Structure
myproject/
│
├── myapp/
│ ├── templates/
│ ├── static/
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── myproject/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
├── requirements.txt
└── Procfile

---

## ⚙️ Installation (Local Setup)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/cafe-website.git
cd cafe-website
### Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

Run server
python manage.py runserver

🌍 Deployment (Railway)

Push project to GitHub

Connect GitHub repo to Railway

Add PostgreSQL service

Set environment variables:

DATABASE_URL

DEBUG=False

Deploy 🚀
