import os


class Library:
    def __init__(self):
        self.file_path = os.path.join("books.txt")
        self.file = open(self.file_path, "a+")
        print("""
██╗     ███╗   ███╗███████╗
██║     ████╗ ████║██╔════╝
██║     ██╔████╔██║███████╗
██║     ██║╚██╔╝██║╚════██║
███████╗██║ ╚═╝ ██║███████║
╚══════╝╚═╝     ╚═╝╚══════╝                                                                                                                                                                                                                                                                           
""")
        print("Welcome to The Library Management System")

    def close(self):
        self.file.close()

    def list_books(self):
        try:
            self.file.seek(0)
            lines = self.file.read().splitlines()
            for line in lines:
                book_info = line.split(',')
                print(
                    f"Title: {book_info[0]} / Author: {book_info[1]} / Publish Date: {book_info[2]} / Page: {book_info[3]}  ")
        except KeyboardInterrupt:
            print("\n Returning to main menu...")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter book release date: ")
        num_pages = input("Enter book number of pages: ")
        self.file.write(f"{title},{author},{release_date},{num_pages}\n")

    def remove_book(self):
        try:
            while True:
                title = input("Enter book title to remove: ").strip()
                if not title:
                    print("Book is not in the list. Try another book to delete.")
                    continue

                self.file.seek(0)
                lines = self.file.readlines()
                updated_books = [line for line in lines if title not in line.strip()]

                self.file.seek(0)
                self.file.truncate()
                self.file.writelines(updated_books)
                print(f"'{title}' was deleted.")
                break
        except KeyboardInterrupt:
            print("\n Returning to main menu...")
