# Author : Shibin Shaji, Yiwei Li
# Date : 06, Feb 2025
# Description : a program that can store and retrieve information related to a user's reading list.

import csv


# Function to add a book to the reading list with input validation
def add_book(title, author, year):
    try:
        title = title.strip()
        if title == "":
            raise ValueError("Title cannot be empty.")

        author = author.strip()
        if author == "":
            raise ValueError("Author name cannot be empty.")

        year = year.strip()
        if year.isdigit() is False or int(year) < 0:
            raise ValueError("Year must be a positive integer.")

        with open('books.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
        print("Book added successfully!")
    except ValueError as e:
        print(f"Error: {e}")


# Function to list all books
def list_books():
    try:
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            books = list(reader)
            if not books:
                print("No books found.")
                return
            for row in books:
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    except FileNotFoundError:
        print("No books found. The file does not exist.")


# Function to search for a book by title
def search_book(title):
    try:
        title = title.strip()
        if title == "":
            raise ValueError("Title cannot be empty.")

        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                    return
        print("Book not found.")
    except FileNotFoundError:
        print("No books found. Please add books first.")
    except ValueError as e:
        print(f"Error: {e}")


# Function to delete a book by title
def delete_book(title):
    try:
        title = title.strip()
        if title == "":
            raise ValueError("Title cannot be empty.")

        books = []
        found = False
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() != title.lower():
                    books.append(row)
                else:
                    found = True

        if found:
            with open('books.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(books)
            print("Book deleted successfully!")
        else:
            print("Book not found.")
    except FileNotFoundError:
        print("No books found. Please add books first.")
    except ValueError as e:
        print(f"Error: {e}")


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


# Run the program
if __name__ == "__main__":
    menu()
