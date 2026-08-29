# 📝 Todo List Web Application

A simple and responsive task management web application built with **Python and Django**.

This project was created to practice building a complete web application with **user authentication, CRUD operations, database management, and deployment**.

## 🌐 Live Demo

🚀 **[View the Live Application](https://todolist-ai-lms1.vercel.app/)**

---

## ✨ Features

- 🔐 **User Authentication** — Register, login, and logout
- ➕ **Create Tasks** — Add new tasks to your list
- 👀 **View Tasks** — View your tasks and individual task details
- ✏️ **Update Tasks** — Edit existing tasks
- 🗑️ **Delete Tasks** — Remove tasks when they are no longer needed
- 👤 **User-based Tasks** — Users can manage their own tasks
- 💾 **Database Storage** — Tasks and user information are stored in a database

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 **Python** | Backend programming |
| 🌐 **Django** | Web framework |
| 🎨 **HTML & CSS** | Frontend and styling |
| 🗄️ **SQLite** | Local development database |
| 🐘 **PostgreSQL** | Production database |
| ☁️ **Neon** | PostgreSQL database hosting |
| ▲ **Vercel** | Deployment |
| 🔧 **Git & GitHub** | Version control |

---

## 📂 Project Structure

```text
todo/
│
├── base/
│   ├── migrations/
│   ├── templates/
│   │   └── base/
│   │       ├── logins.html
│   │       ├── register.html
│   │       ├── main.html
│   │       ├── task.html
│   │       ├── task_form.html
│   │       ├── task_list.html
│   │       └── taskdelete.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── todo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
