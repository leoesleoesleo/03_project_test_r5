# Library
import unittest
from unittest.mock import MagicMock

# Internal
from integration.library import services
from integration.library import exceptions


class TestGoogleBooksService(unittest.TestCase):

    def test_services_google_books_valid_results(self):
        # Mock results
        results = {
            "totalItems": 2,
            "items": [
                {
                    "id": "1",
                    "volumeInfo": {
                        "title": "Book 1",
                        "subtitle": "Subtitle 1",
                        "authors": ["Author 1"],
                        "categories": ["Category 1"],
                        "publishedDate": "2022-01-01",
                        "description": "Description 1",
                        "publisher": "Publisher 1",
                        "imageLinks": "Image Links 1"
                    }
                },
                {
                    "id": "2",
                    "volumeInfo": {
                        "title": "Book 2",
                        "subtitle": "Subtitle 2",
                        "authors": ["Author 2"],
                        "categories": ["Category 2"],
                        "publishedDate": "2022-02-01",
                        "description": "Description 2",
                        "publisher": "Publisher 2",
                        "imageLinks": "Image Links 2"
                    }
                }
            ]
        }

        author_name = "John Doe"

        response = services.services_google_books(
            results=results,
            author_name=author_name
        )

        # validate results
        self.assertEqual(response["source"], "google_books")
        self.assertEqual(response["author_name"], author_name)
        self.assertEqual(response["total_books"], 2)
        self.assertEqual(response["book_title"], ["Book 1", "Book 2"])
        self.assertEqual(response["v_subtitle"], ["Subtitle 1", "Subtitle 2"])
        self.assertEqual(response["v_authors"], [["Author 1"], ["Author 2"]])
        self.assertEqual(response["v_categories"], [["Category 1"], ["Category 2"]])
        self.assertEqual(response["v_publishedDate"], ["2022-01-01", "2022-02-01"])
        self.assertEqual(response["v_description"], ["Description 1", "Description 2"])
        self.assertEqual(response["v_publisher"], ["Publisher 1", "Publisher 2"])
        self.assertEqual(response["v_imageLinks"], ["Image Links 1", "Image Links 2"])

    def test_services_google_books_no_results(self):
        results = {}
        author_name = "John Doe"

        response = services.services_google_books(
            results=results,
            author_name=author_name
        )

        self.assertEqual(response["source"], "google_books")
        self.assertEqual(response["author_name"], author_name)
        self.assertEqual(response["error"], "No Results")

    def test_services_google_books_invalid_data_format(self):
        results = {
            "totalItems": 2,
            "items": []
        }
        author_name = "John Doe"

        response = services.services_google_books(
            results=results,
            author_name=author_name
        )

        self.assertEqual(response["source"], "google_books")
        self.assertEqual(response["author_name"], author_name)
        self.assertEqual(response["error"], "Invalid data format")

    def test_services_google_books_exception_raised(self):
        results = {
            "totalItems": 2,
            "items": [
                {
                    "id": "1",
                    "volumeInfo": {
                        "title": "Book 1",
                        "subtitle": "Subtitle 1",
                        "authors": ["Author 1"],
                        "categories": ["Category 1"],
                        "publishedDate": "2022-01-01",
                        "description": "Description 1",
                        "publisher": "Publisher 1",
                        "imageLinks": "Image Links 1"
                    }
                }
            ]
        }

        author_name = "John Doe"

        exception_mock = exceptions.GoogleBooksDataError("Custom Error")

        pool_mock = MagicMock()
        pool_mock.add_data.side_effect = exception_mock

        response = services.services_google_books(
            results=results,
            author_name=author_name
        )

        self.assertEqual(response["source"], "google_books")
        self.assertEqual(response["author_name"], author_name)
