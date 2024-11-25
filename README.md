
# 🌟 Blog Project

Welcome to the **Django Blog Project**! This application allows users to create, edit, and manage blog posts and comments. Featuring user authentication and a sleek, responsive design, it's a perfect foundation for your blogging platform.

---

## 🚀 Features

✨ User registration and authentication  
✨ Create, edit, and delete blog posts  
✨ Add comments to blog posts  
✨ Responsive templates for an optimal user experience  

---

## 📋 Prerequisites

Before running the project, ensure you have the following installed:

| Prerequisite           | Version    | Notes                           |
|-------------------------|------------|---------------------------------|
| **Python**             | `3.12.2`   | Required                       |
| **pip**                | Latest     | Python package manager         |
| **Virtualenv** (optional) | Any      | Recommended for dependency isolation |

---

## ⚙️ Setup Instructions

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd blog_project
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv myenv
```

### 3️⃣ Activate the Virtual Environment
```bash
# On Windows
.\myenv\Scripts\Activate

# On macOS/Linux
source myenv/bin/activate
```

### 4️⃣ Upgrade pip
```bash
python -m pip install --upgrade pip
```

### 5️⃣ Install Dependencies
```bash
pip install django
pip install pillow
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

Access the application at 👉 `http://127.0.0.1:8000`.

---

## 📂 Directory Structure

Here’s an overview of the main directories:

```plaintext
blog_project/
├── blog/                  # Main application directory
│   ├── migrations/        # Database migration files
│   ├── templates/         # HTML templates for the project
│   ├── static/            # Static assets (CSS, JS, images)
│   ├── models.py          # Database models
│   ├── views.py           # Application views
│   ├── urls.py            # URL configurations
│   └── forms.py           # Forms for the application
├── blog_project/          # Project-level configurations
│   ├── settings.py        # Main settings file
│   ├── urls.py            # Project-level URL configurations
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── manage.py              # Django command-line utility
└── requirements.txt       # Python dependencies
```

---

## 🤝 Contributing

We welcome contributions! 🎉 Fork this repository and submit a pull request with your changes.

---

## 📜 License

This project is licensed under the **MIT License**. See the [`LICENSE`](./LICENSE) file for more details.

---

## 🧑‍💻 Contact

Have questions? Feel free to reach out!  
📧 Email: [sqlpygenius@gmail.com](mailto:sqlpygenius@gmail.com)  
🌐 Website: [https://www.okaydoky.com](https://okaydoky.com)

---
