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

    def test_list_books_with_data(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Book1", "Author1", "2020"])
            writer.writerow(["Book2", "Author2", "2021"])
        self.assertEqual(list_books(), None)

    def test_list_books_empty_file(self):
        open('books.csv', 'w').close()  # Create an empty file
        self.assertEqual(list_books(), None)




if __name__ == "__main__":
    unittest.main()
