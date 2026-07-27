#  Library Management System

A **Django-based Library Management System** developed as an **MCA Mini Project**. This application helps librarians efficiently manage books, students, book issuing, returns, due dates, and overdue fine calculation through a simple and user-friendly interface.

---

##  Features

### Authentication
- Secure Login & Logout

### Book Management
- Add, Edit, Delete Books
- Search Books
- Manage Book Quantity

### Student Management
- Add, Edit, Delete Students
- Search Students

### Book Transactions
- Issue Books
- Return Books
- Automatic 7-Day Due Date
- Automatic Fine Calculation (₹5 per overdue day)
- Overdue Book Detection
- Student Borrowing History

### Dashboard
- Total Books
- Total Students
- Issued Books
- Returned Books
- Available Books

---

##  Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

##  Project Structure

```text
LibraryManagement/
│
├── library/
├── templates/
├── static/
├── manage.py
├── db.sqlite3
└── README.md
```

---

##  Installation

### Clone the repository

```bash
git clone https://github.com/parvathy-A2004/LibraryManagement.git
```

### Move into the project

```bash
cd LibraryManagement
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

##  Screenshots

Add screenshots here after uploading them.

- Dashboard
- Book Management
- Student Management
- Issue Book
- Return Book
- Student History

---

##  Future Enhancements

- Barcode Scanner
- QR Code Integration
- Email Notifications
- PDF Report Generation
- Book Reservation System

---

##  Developer

**Parvathy A**

- GitHub: https://github.com/parvathy-A2004
- LinkedIn: https://www.linkedin.com/in/parvathy-a-187a81337/

---

##  License

This project was developed for educational purposes.

---

⭐ If you found this project useful, consider giving it a star!
