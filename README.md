Тесты на метод add_new_book:
1. test_add_new_book_add_one_book_success - добавляет с названием из 1 символа, из 40 символов, и + позитивная проверка между границами
2. test_add_new_book_long_book_name_add_error - добавляет книгу с названием из 41 символа
3. test_add_new_book_add_one_book_twice_add_error - добавляет одну книгу дважды

Тесты на метод set_book_genre:
4. test_set_book_genre_book_in_books_genre_and_genre_in_genre_success - присваивает жанр, которые есть в списке жанров книге, которая есть в справочнике книг
5. test_set_book_genre_book_not_in_book_genre_set_error - присваивает жанр, которые есть в списке жанров книге, которой нет в справочнике книг
6. test_set_book_genre_genre_not_in_genre_set_error - присваивает жанр, которого нет в списке жанров книге, которая есть в справочнике книг

Тесты на метод get_book_genre:
7. test_get_book_genre_book_in_book_genre_get_genre - получает жанр существующей в справочнике книги с присовоенным ранее жанром
8. test_get_book_genre_book_not_in_book_genre_get_error - получает жанр отсутствующей в справочнике книги

Тесты на метод get_books_with_specific_genre:
9. test_get_books_with_specific_genre_success - получает список книг по жанрам, которые есть в списке жанров, один из них присвоен книге из справочника, другой нет
10. test_get_books_with_specific_genre_genre_not_in_genre_error - получает список книг по жанру, которого нет в списке жанров

Тесты на метод get_books_genre:
11. test_get_books_genre_add_one_book_get_list - получает справочник с одной добавленной книгой
12. test_get_books_genre_add_zero_book_empty_list - получает справочник без добавленных книг

Тесты на метод get_books_for_children:
13. test_get_books_for_children_add_one_book_for_children_get_list - получает одну добавленную книгу без возрастного рейтинга 
14. test_get_books_for_children_add_one_book_for_adult_empty_list - добавляет одну книгу с возрастным рейтингом и получает пустой список книг без возрастного рейтинга 

Тесты на метод add_book_in_favorites:
15. test_add_book_in_favorites_book_in_books_genre_success - добавляет книгу, которая есть в справочнике, в избранное и выводит список избранных книг
16. test_add_book_in_favorites_book_not_in_books_genre_error - добавляет книгу, которой нет в справочнике, в избранное и выводит список избранных книг
17. test_add_book_in_favorites_add_book_twice_add_error - добавляет книгу, которая есть в справочнике, в избранное дважды и выводит список избранных книг

Тесты на метод delete_book_from_favorites:
18. test_delete_book_from_favorites_book_in_favorites_success - удаляет книгу, которая ранее добавлена в избранное, из избранного
19. test_delete_book_from_favorites_book_not_in_favorites_error - удаляет книгу, которая ранее не была добавлена в избранное, из избранного

Тесты на метод get_list_of_favorites_books:
20. test_get_list_of_favorites_books_add_one_book_get_list - добавляет одну книгу в избранное и получает список избранных книг
21. test_get_list_of_favorites_books_add_zero_book_empty_list - не добавляет книг в избранное и получает список избранных книг