from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

	#проверяем, что у любой из добавленных книг нет жанра
    def test_add_new_book_one_book_has_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

	#проверяем, что книге можно установить жанр
    def test_set_book_genre_one_book_can_set_the_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ходячие мертвецы')
        collector.set_book_genre('Ходячие мертвецы', 'Ужасы')
        assert collector.books_genre['Ходячие мертвецы'] == 'Ужасы'

	#проверяем, вывод жанра книги по её имени
    def test_get_book_genre_one_book_its_name(self, collector):
        collector.add_new_book('Шерлок')
        collector.set_book_genre('Шерлок', 'Детективы')
        assert collector.get_book_genre('Шерлок') == 'Детективы'


        #проверяем, вывод списка книг с определенным жанром
    def test_get_books_with_specific_genre_two_horror_book(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        collector.add_new_book('Ходячие мертвецы')
        collector.set_book_genre('Ходячие мертвецы', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Ходячие мертвецы', 'Гордость и предубеждение и зомби']

        #проверяем, что выводится словарь books_genre
    def test_get_books_genre_of_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        collector.add_new_book('Ходячие мертвецы')
        collector.set_book_genre('Ходячие мертвецы', 'Ужасы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_books_genre() == {'Что делать, если ваш кот хочет вас убить' : 'Фантастика', 'Ходячие мертвецы' : 'Ужасы', 'Гордость и предубеждение и зомби' : 'Ужасы'} 

        #проверяем, что выводятся книги, подходящие детям
    def test_get_books_for_children_one_book_display_cartoons(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и медведь')
        collector.set_book_genre('Маша и медведь', 'Мультфильмы')
        collector.add_new_book('Ходячие мертвецы')
        collector.set_book_genre('Ходячие мертвецы', 'Ужасы')
        assert collector.get_books_for_children() == ['Маша и медведь']

        #проверяем, что книга добавляется в избранное
    def test_add_book_in_favorites_one_book_add_to_favorite(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и медведь')
        collector.add_new_book('Ходячие мертвецы')
        collector.add_book_in_favorites('Ходячие мертвецы')
        assert 'Ходячие мертвецы' in collector.favorites


        #проверяем, что книгу можно удалить из избранного
    def test_delete_book_from_favorites_was_deleted_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маша и медведь')
        collector.add_new_book('Ходячие мертвецы')
        collector.add_book_in_favorites('Ходячие мертвецы')
        collector.delete_book_from_favorites('Ходячие мертвецы')
        assert len(collector.favorites) == 0

        #проверяем, вывод списка избранных книг
    def test_get_list_of_favorites_books_got_list(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Ходячие мертвецы')
        collector.add_new_book('Маша и медведь')
        collector.add_book_in_favorites('Ходячие мертвецы')
        collector.add_book_in_favorites('Маша и медведь')
        assert collector.get_list_of_favorites_books() == ['Ходячие мертвецы', 'Маша и медведь']
