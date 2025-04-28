import pytest
from main import BooksCollector
import data 

@pytest.fixture
def add_book():
    collector = BooksCollector()
    collector.add_new_book(data.book_1)
    return collector

@pytest.fixture
def set_book_genre():
    collector = BooksCollector()
    collector.add_new_book(data.book_1)
    collector.set_book_genre(data.book_1, data.genre_in_list_1)
    return collector

@pytest.fixture
def add_favorite_book():
    collector = BooksCollector()
    collector.add_new_book(data.book_1)
    collector.add_book_in_favorites(data.book_1)
    return collector