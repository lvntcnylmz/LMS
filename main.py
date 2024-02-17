from library import Library


def main():
    lib = Library()
    while True:
        print("\n***MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
    lib.close()


if __name__ == "__main__":
    main()
