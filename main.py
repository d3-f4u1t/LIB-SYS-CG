#menu
from ops import *

def menu():
    print("lib management system")
    print("1.add book")
    print("2.show books")
    print("3.issue book")
    print("4.return book")
    print("5.exit")


while True:
    menu()
    c = input("enter your choice")

    if c == "1":
        add_books()

    elif c == "2":
        show_book()

    elif c == "3":

        issue_books()

    elif c == "4":
        return_book()

    elif c == "5":
        print("Exiting...")
        break

    else:
        print("invalid choice")