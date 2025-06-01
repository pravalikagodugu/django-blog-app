# 📝 Django Blogging Platform(DJANGO BLOG POST APPLICATION)
A simple blogging platform built using **Django**. This app allows users to create, read, update, and delete blog posts with images. Admins can manage posts using Django's built-in admin interface.

## 🚀 Features

- Add blog posts with images
- View a list of blog posts
- View individual blog post details
- Edit or delete blog posts
- Admin panel 

## 🛠️ Project Setup

### 📦 Prerequisites

- Python 3.x
- pip
- Django (`pip install django`)
- Pillow (`pip install Pillow`)

### 🧱 Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/django-blogsite.git
   cd django-blogsite
Create Virtual Environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

pip install -r requirements.txt
Or manually:

pip install django pillow
Start the Django Project and App

django-admin startproject blogsite
cd blogsite
python manage.py startapp gallery
📁 File Structure (Overview)

blogsite/
├── blogsite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── gallery/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── myapp/
│           ├── index.html
│           ├── index2.html
│           ├── edit.html
│           └── delete.html
└── media/
⚙️ Configuration
1. models.py (inside gallery/)
   
2. admin.py

3. forms.py

4. views.py

5. gallery/urls.py

6. blogsite/urls.py

- index.html – Main or Home page
- index2.html – Blog Detail View
- edit.html – Edit Form
- delete.html – Delete Confirmation

🧰 Settings Configuration to your settings.py:

⚡ Final Steps
Make Migrations & Migrate

python manage.py makemigrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser
Run Server

python manage.py runserver

Visit
Admin: http://127.0.0.1:8000/admin/

Site: http://127.0.0.1:8000/


