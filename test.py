import pytest
from main import BooksCollector
import data


class TestBooksCollector:

    #тесты на метод add_new_book
    @pytest.mark.parametrize('name', [data.name_1_symbol, data.name_40_symbols, data.book_1])
    def test_add_new_book_add_one_book_success(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1 and collector.get_books_genre() == {name: ''}

    def test_add_new_book_long_book_name_add_error(self):
        collector = BooksCollector()
        collector.add_new_book(data.name_41_symbols)
        assert len(collector.get_books_genre()) == 0
    
    def test_add_new_book_add_one_book_twice_add_error(self, add_book):
        add_book.add_new_book(data.book_1)
        assert len(add_book.get_books_genre()) == 1
    
    #тесты на метод set_book_genre
    def test_set_book_genre_book_in_books_genre_and_genre_in_genre_success(self, add_book):
        add_book.set_book_genre(data.book_1, data.genre_in_list_1)
        assert add_book.get_book_genre(data.book_1) == data.genre_in_list_1

    def test_set_book_genre_book_not_in_book_genre_set_error(self, add_book):
        add_book.set_book_genre(data.book_2, data.genre_in_list_1)
        assert not add_book.get_book_genre(data.book_2)
    
    def test_set_book_genre_genre_not_in_genre_set_error(self, add_book):
        add_book.set_book_genre(data.book_1, data.genre_not_in_list)
        assert add_book.get_book_genre(data.book_1) == ''
    
    #тесты на метод get_book_genre
    def test_get_book_genre_book_in_book_genre_get_genre(self, set_book_genre):
        assert set_book_genre.get_book_genre(data.book_1) == data.genre_in_list_1

    def test_get_book_genre_book_not_in_book_genre_get_error(self, set_book_genre):
        assert not set_book_genre.get_book_genre(data.book_2)

    #тесты на метод get_books_with_specific_genre
    @pytest.mark.parametrize('genre, result', [
        (data.genre_in_list_1, [data.book_1]),
        (data.genre_in_list_2,[])
        ])
    def test_get_books_with_specific_genre_success(self, set_book_genre, genre, result):
        assert set_book_genre.get_books_with_specific_genre(genre) == result

    def test_get_books_with_specific_genre_genre_not_in_genre_error(self, set_book_genre):
        assert not set_book_genre.get_books_with_specific_genre(data.genre_not_in_list)

    #тесты на метод get_books_genre
    def test_get_books_genre_add_one_book_get_list(self, add_book):
        assert add_book.get_books_genre() == {data.book_1:''}

    def test_get_books_genre_add_zero_book_empty_list(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    #тесты на метод get_books_for_children
    def test_get_books_for_children_add_one_book_for_children_get_list(self, set_book_genre):
        assert set_book_genre.get_books_for_children() == [data.book_1]
    
    def test_get_books_for_children_add_one_book_for_adult_empty_list(self, add_book):
        add_book.set_book_genre(data.book_1, add_book.genre_age_rating[0])
        assert add_book.get_books_for_children() == []

    #тесты на метод add_book_in_favorites
    def test_add_book_in_favorites_book_in_books_genre_success(self, add_book):
        add_book.add_book_in_favorites(data.book_1)
        assert add_book.get_list_of_favorites_books() == [data.book_1]

    def test_add_book_in_favorites_book_not_in_books_genre_error(self, add_book):
        add_book.add_book_in_favorites(data.book_2)
        assert add_book.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_add_book_twice_add_error(self, add_book):
        add_book.add_book_in_favorites(data.book_1)
        add_book.add_book_in_favorites(data.book_1)
        assert len(add_book.get_list_of_favorites_books()) == 1

    #тесты на метод delete_book_from_favorites
    def test_delete_book_from_favorites_book_in_favorites_success(self, add_favorite_book):
        add_favorite_book.delete_book_from_favorites(data.book_1)
        assert add_favorite_book.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_in_favorites_error(self, add_favorite_book):
        add_favorite_book.delete_book_from_favorites(data.book_2)
        assert add_favorite_book.get_list_of_favorites_books() == [data.book_1]

    #тесты на метод get_list_of_favorites_books
    def test_get_list_of_favorites_books_add_one_book_get_list(self, add_favorite_book):
        assert add_favorite_book.get_list_of_favorites_books() == [data.book_1]

    def test_get_list_of_favorites_books_add_zero_book_empty_list(self, add_book):
        assert add_book.get_list_of_favorites_books() == []