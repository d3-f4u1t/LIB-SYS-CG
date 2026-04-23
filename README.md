# 📚 Library Management System (Python Mini Project)

A simple **menu-driven Library Management System** built using Python.  
This project follows **modular programming** and simulates basic real-world library operations.

---

## 🚀 Features

- 📖 Add new books  
- 📚 View available books  
- 🙋 Issue books to students  
- 🔄 Return books  
- 💰 Automatic fine calculation for late returns  
- 🔁 Infinite loop menu system  

---

## 🧠 Concepts Used

- Python Functions  
- Lists & Dictionaries  
- Modular Programming  
- File Separation (Clean Architecture)  
- `datetime` module (for date tracking)  

---

## 📁 Project Structure

'''library_project/
│
├── main.py
├── database.py
├── operations.py
'''

---

## ⚙️ How It Works

### 🔹 Book Storage
- Books are stored in a **list**
- Issued books stored in a **dictionary** with:
  - Student name
  - Issue date
  - Allowed days

### 🔹 Issue System
- Book is removed from available list
- Stored with student details

### 🔹 Return System
- Calculates how many days book was used
- Applies **progressive fine**:
  - Day 1 → ₹10  
  - Day 2 → ₹20  
  - Day 3 → ₹30  
  - and so on...

---

## ▶️ How to Run

1. Open terminal in project folder  
2. Run:
