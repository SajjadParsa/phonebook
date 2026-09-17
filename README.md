# 📱 Phonebook Management System

A simple **Phonebook Management System** built with **Python** and **MariaDB**.

This project allows users to store, search, update, and delete contacts using a command-line interface.

## 🚀 Features

* ➕ Add a new contact
* 📋 Show all contacts
* 🔍 Search contacts by name
* ✏️ Update contact information
* 🗑️ Delete one contact
* 🧹 Delete all contacts
* ❌ Exit the program
* 🗄️ Store data using MariaDB
* ⚠️ Basic input validation and error handling

## 🛠️ Technologies

* Python
* MariaDB
* MariaDB Connector/Python
* SQL

## 📂 Project Structure

```text
Phonebook/
│
├── main.py
├── phonebook.sql
├── requirements.txt
└── README.md
```

## ⚙️ Requirements

Before running the project, make sure you have:

* Python installed
* MariaDB Server installed
* MariaDB running on your computer

## 📥 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then enter the project folder:

```bash
cd Phonebook
```

### 2. Install Python dependency

```bash
pip install -r requirements.txt
```

### 3. Create the database

Open MariaDB or your SQL client and run the `phonebook.sql` file.

The SQL file creates:

* `phonebook` database
* `contacts` table

The table contains:

| Column | Type         | Description       |
| ------ | ------------ | ----------------- |
| id     | INT          | Unique contact ID |
| name   | VARCHAR(100) | Contact name      |
| phone  | VARCHAR(30)  | Phone number      |
| adress | VARCHAR(255) | Contact address   |
| gmail  | VARCHAR(100) | Contact Gmail     |

### 4. Check database connection

The Python program currently uses:

```python
host="localhost"
port=3306
user="root"
password=""
database="phonebook"
```

If your MariaDB username or password is different, change these values in `main.py`.

### 5. Run the program

```bash
python main.py
```

## 📋 Main Menu

```text
1. Add contact
2. Show contacts
3. Search contact
4. Update contact
5. Delete contact
6. Exit
```

## ✏️ Update Options

The program provides several ways to update a contact:

```text
1. Update name
2. Update name and phone number
3. Update Address and Gmail
4. Update All
5. Back
```

## 🗑️ Delete Options

You can either delete one contact by ID or remove all contacts.

```text
1. Delete a contact
2. Delete all contact
3. Back
```

## 🎯 Purpose of the Project

This project was created as a practice project to learn how to connect Python with a relational database and perform basic CRUD operations.

CRUD means:

* **Create** → Add contact
* **Read** → Show/Search contact
* **Update** → Modify contact
* **Delete** → Remove contact

## 📚 What I Practiced

Through this project, I practiced:

* Python functions
* Loops and conditions
* Exception handling
* User input validation
* SQL queries
* MariaDB
* Python database connections
* CRUD operations
* Basic project structure

## 🔮 Future Improvements

Possible improvements for future versions:

* Search by phone number
* Search by Gmail
* Better input validation
* Better user interface
* Confirmation before deleting a contact
* Prevent duplicate contacts
* Separate database functions from the main menu
* Configuration file for database credentials
* More advanced search functionality

## 👨‍💻 Author

**Sajad Parsa**

A Python and Computer Science student working on practical projects to improve programming and AI  development.
