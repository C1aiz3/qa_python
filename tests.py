import pytest


class TestBooksCollector:

    def test_initialization_books_collector_true(self, test_book):
        assert test_book.books_genre == {}
        assert test_book.favorites == []
        assert test_book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert test_book.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Шерлок Холмс', 'Человек-паук: Через вселенные'])
    def test_add_new_book_add_book(self, test_book, name):
        test_book.add_new_book(name)
        assert name in test_book.books_genre

    @pytest.mark.parametrize('name, genre', [['Гарри Поттер', 'Фантастика'], ['Шерлок Холмс', 'Детективы'],
                                             ['Человек-паук: Через вселенные', 'Мультфильмы']])
    def test_set_book_genre_set_books_genre(self, test_book, name, genre):
        test_book.add_new_book(name)
        test_book.set_book_genre(name, genre)
        assert test_book.books_genre[name] == genre

    @pytest.mark.parametrize('name, genre',
                             [['Гарри Поттер', 'Фантастика'],
                              ['Шерлок Холмс', 'Детективы'],
                              ['Человек-паук: Через вселенные', 'Мультфильмы']
                              ])
    def test_get_book_genre_get_book_genre(self, test_book, name, genre):
        test_book.add_new_book(name)
        test_book.set_book_genre(name, genre)
        assert genre == test_book.get_book_genre(name)

    @pytest.mark.parametrize('name, genre',
                             [['Гарри Поттер', 'Фантастика'],
                              ['Игра Эндера', 'Фантастика'],
                              ['Первому игроку приготовится', 'Фантастика'],
                              ['Шерлок Холмс', 'Детективы']
                              ])
    def test_get_books_with_specific_genre_get_books_same_genre(self, test_book, name, genre):
        test_book.add_new_book(name)
        test_book.set_book_genre(name, genre)
        assert 'Шерлок Холмс' not in test_book.get_books_with_specific_genre('Фантастика')

    def test_get_books_genre_dict_true(self, test_book):
        assert type(test_book.get_books_genre()) == dict

    @pytest.mark.parametrize('name, genre',
                             [['Гарри Поттер', 'Фантастика'],
                              ['Игра Эндера', 'Фантастика'],
                              ['Первому игроку приготовится', 'Фантастика'],
                              ['Шерлок Холмс', 'Детективы']
                              ])
    def test_get_books_for_children_book_not_in_list(self, test_book, name, genre):
        test_book.add_new_book(name)
        test_book.set_book_genre(name, genre)
        assert 'Шерлок Холмс' not in test_book.get_books_for_children()

    def test_add_book_in_favorites_empty_true(self, test_book):
        assert test_book.favorites == []

    def test_add_book_in_favorites_add_book(self, test_book):
        test_book.add_new_book('Гарри Поттер')
        test_book.set_book_genre('Гарри Поттер', 'Фантастика')
        test_book.add_book_in_favorites('Гарри Поттер')
        assert 'Игра Эндера' not in test_book.favorites

    def test_delete_book_from_favorites_delete_book(self, test_book):
        test_book.add_new_book('Гарри Поттер')
        test_book.set_book_genre('Гарри Поттер', 'Фантастика')
        test_book.add_book_in_favorites('Гарри Поттер')
        test_book.delete_book_from_favorites('Гарри Поттер')
        assert test_book.favorites == []

    @pytest.mark.parametrize('name, genre',
                             [['Гарри Поттер', 'Фантастика'],
                              ['Игра Эндера', 'Фантастика'],
                              ['Первому игроку приготовится', 'Фантастика']
                              ])
    def test_get_list_of_favorites_books_books_in_favorites_list(self, test_book, name, genre):
        test_book.add_new_book(name)
        test_book.set_book_genre(name, genre)
        test_book.add_book_in_favorites(name)
        assert name in test_book.get_list_of_favorites_books()