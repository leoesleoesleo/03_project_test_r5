# Django
from django.test import TestCase
from unittest.mock import patch

# Internal
from integration.customer.models import Customer
from integration.library.models import (
    Book, 
    Author, 
    Category, 
    Published, 
    BookAuthor, 
    BookCategory
)
from integration.library import services


class LibraryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(
            id=1,
            external_id=1,
            user=1,
            phone="300",
            email="test@gmail.com",
            extra_data={"location": "test", "office_hours": "test"},
            is_active=1
        )

        Customer.objects.create(
            id=2,
            external_id=2,
            user=2,
            phone="900",
            email="test2@gmail.com",
            extra_data={"location": "test2", "office_hours": "test2"},
            is_active=1
        )

        Customer.objects.create(
            id=3,
            external_id=3,
            user=3,
            phone="800",
            email="test3@gmail.com",
            extra_data={"location": "test3", "office_hours": "test3"},
            is_active=1
        )

        Author.objects.create(
            id=1,
            first_name="John",
            last_name="Doe"
        )

        Author.objects.create(
            id=2,
            first_name="Jane",
            last_name="Smith"
        )
        
        Category.objects.create(
            id=1,
            name="Fiction"
        )

        Category.objects.create(
            id=2,
            name="Mystery"
        )
        
        Published.objects.create(
            id=1,
            name="Publisher A"
        )

        Published.objects.create(
            id=2,
            name="Publisher B"
        )
        
        Book.objects.create(
            id=1,
            title="Book A",
            subtitle="",
            publication_date="2023-01-01",
            description="This is book A.",
            image="",
            editor_id=1
        )

        Book.objects.create(
            id=2,
            title="Book B",
            subtitle="",
            publication_date="2023-02-01",
            description="This is book B.",
            image="",
            editor_id=2
        )
        
        book_a = Book.objects.get(id=1)
        author_a = Author.objects.get(id=1)

        BookAuthor.objects.create(
            book=book_a,
            author=author_a
        )

        book_b = Book.objects.get(id=2)
        author_b = Author.objects.get(id=2)

        BookAuthor.objects.create(
            book=book_b,
            author=author_b
        )
        
        book_a = Book.objects.get(id=1)
        category_a = Category.objects.get(id=1)

        BookCategory.objects.create(
            book=book_a,
            category=category_a
        )

        book_b = Book.objects.get(id=2)
        category_b = Category.objects.get(id=2)

        BookCategory.objects.create(
            book=book_b,
            category=category_b
        )

    @patch('integration.library.selectors.list_books_by_author')
    def test_list_book_by_author(self, mock_list_books_by_author):
        author = "John Doe"
        mock_books = [
            "Book A",
            "Book B",
            "Book C"
        ]
        mock_list_books_by_author.return_value = mock_books

        expected_result = {
            "source": "bd_interna",
            "author_name": author,
            "total_books": len(mock_books),
            "book_title": mock_books
        }

        result = services.list_book_by_author(author=author)

        self.assertEqual(result, expected_result)
        mock_list_books_by_author.assert_called_once_with(author=author)

    def test_service_delete_book_by_id_success(self):
        result = services.service_delete_book_by_id(id=1)
        self.assertTrue(result)
