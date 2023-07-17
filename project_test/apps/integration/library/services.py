# Libraries
from concurrent.futures import ThreadPoolExecutor
from django.db import transaction
from django.shortcuts import get_object_or_404
import asyncio
from asgiref.sync import sync_to_async

# Internal
from integration.api_google_books.connector import GoogleBooksConnector
from integration.api_open_library.connector import OpenLibraryConnector
from integration.library import selectors
from integration.library.pool_response_api import PoolResponse
from integration.library.models import (
    Book, 
    Author, 
    Category, 
    Published, 
    BookAuthor, 
    BookCategory
)
from integration.library import exceptions
from integration.library.constants import (
    ResponseExceptions,
    ApiGoogle,
    OpenLibrary,
    BdInterna
)


pool = PoolResponse()


def services_google_books(
    *,
    results: dict,
    author_name: str
) -> dict:
    try:
        if not results:
            raise exceptions.GoogleBooksDataError(
                ResponseExceptions.NORESULTS.value
            )

        total_books = results.get("totalItems", 0)
        items = results.get("items", [])
        if not items:
            raise exceptions.GoogleBooksDataError(
                ResponseExceptions.INVALIDFORMAT.value
            )

        v_book_title = []
        v_subtitle = []
        v_authors = []
        v_categories = []
        v_publishedDate = []
        v_description = []
        v_publisher = []
        v_imageLinks = []
        id = None

        for item in items:
            id = item.get("id")
            volume_info = item.get("volumeInfo", {})
            v_book_title.append(
                volume_info.get("title", ApiGoogle.UNKNOWN.value)
            )
            v_subtitle.append(
                volume_info.get("subtitle", ApiGoogle.UNKNOWN.value)
            )
            v_authors.append(
                volume_info.get("authors", ApiGoogle.UNKNOWN.value)
            )
            v_categories.append(
                volume_info.get("categories", ApiGoogle.UNKNOWN.value)
            )
            v_publishedDate.append(
                volume_info.get("publishedDate", ApiGoogle.UNKNOWN.value)
            )
            v_description.append(
                volume_info.get("description", ApiGoogle.UNKNOWN.value)
            )
            v_publisher.append(
                volume_info.get("publisher", ApiGoogle.UNKNOWN.value)
            )
            v_imageLinks.append(
                volume_info.get("imageLinks", ApiGoogle.UNKNOWN.value)
            )

        response = {
            "source": ApiGoogle.SOURCE.value,
            "id_api_google": id,
            "author_name": author_name,
            "total_books": total_books,
            "book_title": v_book_title,
            "v_subtitle": v_subtitle,
            "v_authors": v_authors,
            "v_categories": v_categories,
            "v_publishedDate": v_publishedDate,
            "v_description": v_description,
            "v_publisher": v_publisher,
            "v_imageLinks": v_imageLinks
        }

        # Agregar datos al pool
        pool.add_data(id, response)

        return response

    except exceptions.GoogleBooksDataError as e:
        return {
            "source": ApiGoogle.SOURCE.value,
            "author_name": author_name,
            "error": str(e)
        }


def services_open_library(
    *,
    results: dict,
    author_name: str
) -> dict:
    if results:
        total_books = results["numFound"]
        v_book_title = []        
        docs = results["docs"]
        for doc in docs:
            book_title = doc.get(
                "title", ApiGoogle.UNKNOWN.value
            )
            v_book_title.append(book_title)
        return {
            "source": OpenLibrary.SOURCE.value,
            "author_name": author_name,
            "total_books": total_books,
            "book_title": v_book_title
        } 
    else:
        return {
            "source": OpenLibrary.SOURCE.value,
            "author_name": author_name,
            "total_books": BdInterna.NO_RESULTS.value,
            "book_title": BdInterna.NO_RESULTS.value
        }


def services_apis_pool_executor(
    *,
    author: str
) -> list:
    connector_google_books = GoogleBooksConnector()
    connector_open_library = OpenLibraryConnector()
    
    # Make concurrent requests to both APIs
    with ThreadPoolExecutor() as executor:
        # Add the requests to the parallel work list
        results_google_books = executor.submit(
            connector_google_books.search_books_by_author, author
        ).result()
        
        results_open_library = executor.submit(
            connector_open_library.search_books_by_author, author
        ).result()

        results_google_books = services_google_books(
            results=results_google_books,
            author_name=author
        )
        
        results_open_library = services_open_library(
            results=results_open_library,
            author_name=author
        )

        return [results_google_books, results_open_library]
    

def list_book_by_author(
    *,
    author: str
) -> dict:
    books = selectors.list_books_by_author(
        author=author
    )
    books = [str(book) for book in books]
    return {
            "source": BdInterna.SOURCE.value,
            "author_name": author,
            "total_books": len(books),
            "book_title": books
        }


def service_main_library(
    *,
    author: str
) -> list:
    books = list_book_by_author(
        author=author
    )
    if books.get("total_books"):
        return books
    else:
        return services_apis_pool_executor(
            author=author
        )


async def save_data_asynchronously(
    *,
    json_data: dict
):
    # save asynchronous functions
    await save_authors(
        authors=json_data['v_authors']
    )
    await save_categories(
        categories=json_data['v_categories']
    )
    await save_editors(
        editors=json_data['v_publisher']
    )
    await save_books(json_data=json_data)


async def save_author(
    *,
    author_name: str
):
    author, _ = await sync_to_async(
        Author.objects.get_or_create
    )(first_name=author_name)
    return author


async def save_authors(
    *,
    authors: list
):
    unique_authors = set()
    for author_list in authors:
        if isinstance(author_list, list):
            unique_authors.update(author_list)
        else:
            unique_authors.add(author_list)
    tasks = []
    for author_name in unique_authors:
        task = save_author(
            author_name=author_name
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


async def save_category(
    *,
    category_name: str
):
    category, _ = await sync_to_async(
        Category.objects.get_or_create
    )(name=category_name)
    return category


async def save_categories(
    *,
    categories: list
):
    unique_categories = set()
    for category_list in categories:
        if isinstance(category_list, list):
            unique_categories.update(category_list)
        else:
            unique_categories.add(category_list)
    tasks = []
    for category_name in unique_categories:
        task = save_category(
            category_name=category_name
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


async def save_editor(
    *,
    editor_name: str
):
    editor, _ = await sync_to_async(
        Published.objects.get_or_create
    )(name=editor_name)
    return editor


async def save_editors(
    *,
    editors: list
):
    unique_editors = set()
    for editor_name in editors:
        if editor_name is not None:
            unique_editors.add(editor_name)
    tasks = []
    for editor_name in unique_editors:
        task = save_editor(
            editor_name=editor_name
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


async def save_book(
    *,
    json_data: dict,
    index: int
):
    title = json_data['book_title'][index]
    subtitle = json_data['v_subtitle'][index]
    publication_date = json_data['v_publishedDate'][index]
    description = json_data['v_description'][index]
    image_link = str(json_data['v_imageLinks'][index])
    editor_name = json_data['v_publisher'][index]

    # Get or create the publisher
    editor, _ = await sync_to_async(Published.objects.get_or_create)(name=editor_name)

    # Create book
    book, _ = await sync_to_async(Book.objects.get_or_create)(
        title=title,
        subtitle=subtitle,
        publication_date=publication_date,
        description=description,
        editor=editor,
        image=image_link
    )

    # Save Book Authors
    authors = json_data['v_authors'][index]
    for author_name in authors:
        first_name = author_name
        author, _ = await sync_to_async(Author.objects.get_or_create)(
            first_name=first_name
        )
        await sync_to_async(BookAuthor.objects.get_or_create)(
            book=book,
            author=author
        )

    # Save book categories
    categories = json_data['v_categories'][index]
    if categories is not None:
        for category_name in categories:
            category, _ = await sync_to_async(Category.objects.get_or_create)(name=category_name)
            await sync_to_async(BookCategory.objects.get_or_create)(
                book=book,
                category=category
            )


async def save_books(
    *,
    json_data: dict
):
    tasks = []
    for i in range(len(json_data['book_title'])):
        task = save_book(
            json_data=json_data,
            index=i
        )
        tasks.append(task)
    await asyncio.gather(*tasks)


def service_save_library(
    *,
    id: str,
    source: str
) -> dict:
    if source == ApiGoogle.SOURCE.value:
        # Get pool data
        recovered = pool.get_data(id)
        if recovered:            
            asyncio.run(save_data_asynchronously(
                json_data=recovered
            ))
            recovered["Response"] = BdInterna.SAVE_DATA.value
            return recovered
    return {
        "Response": BdInterna.NO_RESULTS.value
    }


@transaction.atomic
def service_delete_book_by_id(
    *,
    id: int
):
    try:
        book = get_object_or_404(Book, id=id)
        book.delete()
        return True
    except Book.DoesNotExist:
        return False
