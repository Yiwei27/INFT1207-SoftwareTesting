import csv
import unittest
from Lab2_Shibin_Yiwei import add_book, list_books, search_book, delete_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        #1. Test adding a book.
        add_book("Test Book", "Author Name", "2022")  # Now passes arguments directly

        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        self.assertIn(["Test Book", "Author Name", "2022"], rows)

    def test_add_book_multiple_entries(self):
        add_book("Book1", "Author1", "2020")
        add_book("Book2", "Author2", "2021")
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            books = list(reader)
        self.assertIn(["Book1", "Author1", "2020"], books)
        self.assertIn(["Book2", "Author2", "2021"], books)

    def test_list_books_with_data(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book1", "Author1", "2020"])
            writer.writerow(["Book2", "Author2", "2021"])
        self.assertEqual(list_books(), None)

    def test_list_books_empty_file(self):
        open('books.csv', 'w').close()  # Create an empty file
        self.assertEqual(list_books(), None)

    def test_list_books_no_file(self):
        self.assertEqual(list_books(), None)

    def test_search_existing_book(self):
        search_book("hello")  # Calls the function (prints output)
        # Open books.csv and verify that "Test Book" is in it
        with open('books.csv', "r") as file:
            reader = csv.reader(file)
            books = list(reader)

        self.assertIn(["hello", "tio", "2001"], books, "The book was not found in books.csv.")

    def test_search_nonexistent_book(self):
        # Ensure books.csv exists but do NOT erase content
        with open('books.csv', mode='a', newline='') as file:
            pass  # This just makes sure the file exists
        # Call the search function with a book that doesn't exist
        result = search_book("Titanic")
        # Assert that the result is "Book not found."
        self.assertEqual(result, "Book not found.")

    def test_search_empty_title(self):
        # Test with an empty string as the title
        result = search_book("")
        expected_output = "Error: Title cannot be empty."
        self.assertEqual(result, expected_output,
                         "search_book did not return 'Title cannot be empty.' for an empty title.")


    def test_delete_book_success(self):
        delete_book("hello")  # Attempt to delete "hello"
        # Open the books.csv and check that "hello" was deleted
        with open('books.csv', mode='r') as file:
            reader = csv.reader(file)
            books = list(reader)
        # Debugging: Print out the books to verify the file content after deletion
        print("Books after deletion: ", books)
        # Assert that "hello" is no longer in the list
        self.assertNotIn(["hello"], books, "Book 'hello' was not deleted successfully.")

    def test_delete_book_not_found(self):
        result = delete_book("Fast")  # Capture return value
        self.assertEqual(result, "Book not found.",
                         "delete_book did not return 'Book not found.' when the book was missing.")

if __name__ == "__main__":
    unittest.main()
