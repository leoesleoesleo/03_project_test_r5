# Django
from django.db.models import QuerySet
from integration.library.models import Book


def list_books_by_author(
    *, 
    author: str
) -> 'QuerySet[Book]':
    author = author.title()
    return Book.objects.filter(
        bookauthor__author__first_name=author
    )
