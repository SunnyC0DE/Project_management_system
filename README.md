# 📋 Project Management System – Django

A full-stack web application built using the Django framework that allows users to manage multiple projects and tasks with login authentication and role-based access. Ideal for team collaboration and personal productivity.

---

## 📌 Description

This Project Management System provides a structured way to create, view, edit, and delete projects and their associated tasks. Each user can log in, manage their own tasks, and view project progress. Admins can manage all users and content using Django’s built-in admin panel.

---

## 🧠 Features

- User registration and login system
- Create, update, and delete projects
- Assign tasks to users
- Mark task completion and project progress
- Admin dashboard (Django admin)
- Secure session handling

---

## 📂 Project Structure

# webapp
-----        06-04-2025     13:21                apple
-----        06-04-2025     21:39                communication
-----        06-04-2025     17:51                dashboard
-----        06-04-2025     16:28                items
-----        05-04-2025     22:28                media
-----        05-04-2025     13:10                webapp
----        10-04-2025     11:03         188416 db.sqlite3
----        05-04-2025     13:02            684 manage.py


# webapp -> apple

-----                       migrations
-----                       templates
-----                        __pycache__
----                       admin.py
----                      apps.py
----                   forms.py
----                   models.py
----                   tests.py
----                   urls.py
----                   views.py
----                  __init__.py


# webapp -> communication
-----        migrations
-----         templates
-----         __pycache__
----         admin.py
----         apps.py
----         forms.py
----         models.py
----         tests.py
----         urls.py
----         views.py
----         __init__.py


# webapp -> dashboard
-----        migrations
-----        templates
-----        __pycache__
----        admin.py
----        apps.py
----        models.py
----        tests.py
----        urls.py
----        views.py
----         __init__.py

# webapp -> items
     
-----        migrations
-----        templates
-----        __pycache__
----        admin.py
----        apps.py
----        forms.py
----        models.py
----        tests.py
----         urls.py
----        views.py
----        __init__.py


# webapp -> media

-----  item_images


---

## 🔧 Technologies Used

- Python 3
- Django
- SQLite (default)
- HTML, CSS (Bootstrap for styling)
- Optional: Django Messages, Form Validation, Sessions

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/SunnyC0DE/Project-management-system.git
cd project-management-django

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate # on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

