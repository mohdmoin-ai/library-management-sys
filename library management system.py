books = {}

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        book = input("Enter Book Name: ")

        books[book] = True

        print("Book Added Successfully")

    elif choice == "2":

        book = input("Enter Book Name: ")

        if book in books:
            print("Book Found")
        else:
            print("Book Not Found")

    elif choice == "3":

        book = input("Enter Book Name: ")

        if book in books and books[book]:
            books[book] = False
            print("Book Borrowed")

        else:
            print("Book Not Available")

    elif choice == "4":

        book = input("Enter Book Name: ")

        if book in books:
            books[book] = True
            print("Book Returned")

        else:
            print("Book Not Found")

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")