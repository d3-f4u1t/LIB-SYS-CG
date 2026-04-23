from database import books, issued_books
from datetime import datetime

def add_books():
    name = input("Enter book name:").lower()

    if name in books:
        print("books already exists\n")

    else:
        books.append(name)
        print("book added\n")


#for showing books

def show_book():
    print("\n available books:")

    if not books:
        print("no books available\n")

    else:
        for b in books:
            print(f"{b.title()}")

    print()

#to issue books

def issue_books():
    name = input("Enter the book name").lower()

    if name in books:
        student = input("Enter student name").title()
        days = int(input("for how many days:"))

        books.remove(name)

        issued_books[name] = {
            "student": student,
            "date": datetime.now(),
            "days": days
        }

        print(f"'{name}' issued to {student} for {days} days\n")

    else:
        print("book not available\n")


#to return books

def return_book():
    name = input("Enter the book name").lower()


    if name in issued_books:
        record = issued_books[name]

        issue_date = record["date"]

        allowed_days = record["days"]

        return_date = datetime.now()

        days_used = (return_date - issue_date).days

        fine = calculate_fine(days_used, allowed_days)

        print(f"days used: {days_used}")
        print(f"fine: RS {fine}")

        books.append(name)

        del issued_books[name]

        print(f"'{name}'returned successfully\n")

    else:
        print("This book is not issued\n")

#for fine calculation

def calculate_fine(days_used, allowed_days):
    extra_days = days_used - allowed_days

    if extra_days <= 0:
        return 0
    
    fine = 0

    base_rate = 10

    for i in range(1, extra_days+1):
        fine += base_rate * i 

    return fine