#  ╔════════════════════════════════════════════╗
#  ║            🌐 MYPROJ Django App            ║
#  ║         ASCII-Style Project README        ║
#  ╚════════════════════════════════════════════╝

      .-.
     (   )   _
      `-`  .' )
          /  /
         /  /   .-.
        /  /   (   )
       /  /     `-`
      /__/

##  ✦ Project Overview

This project is a simple Django web application built with a clean multi-page layout.
It includes pages for Home, About, Contact, and a shared base template.

##  ✦ Features

- Responsive page structure with reusable templates
- Home, About, and Contact views
- Clean Django URL routing
- Styled static CSS support

##  ✦ Project Structure

```text
myproj/
├── manage.py
├── db.sqlite3
├── customerApp/
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   └── contact.html
│   ├── static/css/style.css
│   ├── urls.py
│   └── views.py
└── myproj/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

##  ✦ Getting Started

### 1. Install dependencies

```bash
pip install django
```

### 2. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

##  ✦ Available Routes

```text
/        -> Home page
/home/   -> Home page
/about/  -> About page
/contact/ -> Contact page
```

##  ✦ Notes

This app is a great starting point for learning Django templates, URL mapping,
and basic web app structure.

--------------------------------------------
          Made with Django and ASCII charm
--------------------------------------------
