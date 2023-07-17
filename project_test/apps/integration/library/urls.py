# Django
from django.urls import path

# Internal
from integration.library.view import LibraryViews

urlpatterns = [
    path(
        'books_author',
        LibraryViews.as_view(),
        name='books_author'
    )
]
