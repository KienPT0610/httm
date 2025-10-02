# Machine Learning Admin Server

This project is a **Flask-based web server** for managing
Machine Learning pipeline (Admins, Datasets, Samples, Models, Training Jobs).  
It is built with **Python 3.13.3** and uses **MySQL**

---

## Folder Structure

```
Root/
├── client/
│   ├── templates/             # HTML giao diện (Flask Jinja2)
│   │   ├── login.html
│   │   └── dashboard.html
│   │
│   └── static/
├── server/
│   ├── __init__.py
│   ├── main.py                # entry point (chạy app Flask)
│   │
│   ├── controller/
│   │   ├── __init__.py
│   │   └── server_controller.py
│   │
│   ├── dao/
│   │   ├── __init__.py
│   │   ├── dao.py             # BaseDAO
│   │   └── admin_dao.py       # AdminDAO
│   │
│   └── entity/
│       ├── __init__.py
│       └── admin.py           # dataclass Admin
│
└── requirements.txt

```

---

## 📦 Requirements

- Python 3.13.3
- MySQL 8.x (or MariaDB)
- MySQL Workbench (optional, for DB management)

---

## Install Package

```
pip install -r requirements.txt
```

## Run Server

```
python -m server.main
```
