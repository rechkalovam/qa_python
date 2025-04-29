import pytest
from main import BooksCollector
import data 

@pytest.fixture
def add_book():
    collector = BooksCollector()
    collector.add_new_book(data.book_1)
    return collector

@pytest.fixture
def set_book_genre(add_book):
    add_book.set_book_genre(data.book_1, data.genre_in_list_1)
    return add_book

@pytest.fixture
def add_favorite_book(add_book):
    add_book.add_book_in_favorites(data.book_1)
    return add_book