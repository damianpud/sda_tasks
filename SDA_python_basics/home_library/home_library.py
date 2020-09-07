import random
from SDA_python_basics.home_library.data import *
from SDA_python_basics.home_library.save_to_file import *

menu = ("Wyjscie", "Dodaj Ksiazke", "Wyswietl Ksiazki", "Usun Ksiazke")
book_list = {}


def show_menu_list():
    for index in range(len(menu)):
        print(f"{index}. {menu[index]}")


def get_menu():
    while True:
        try:
            value = input("Wybierz z menu: ")
            if value == "q" or value == "Q":
                return 0
            num_value = int(value)

            if num_value in range(len(menu)):
                return num_value
            print("Podales niepoprawny klucz")
        except Exception:
            print("Bad input number value")


def get_input_key():
    while True:
        try:
            key = input("Ktora ksiazke usunac - podaj klucz: ")
            for book in book_list:
                if book == key:
                    return key
            print("Podales niepoprawny klucz")
        except Exception:
            print("Bad input key value")


def get_input_book_value(text):
    while True:
        try:
            return input(text)
        except Exception:
            print("Bad input key value")


def get_book_to_delete():
    show_books(book_list)
    return get_input_key()


def generate_isbn():
    return random.randint(0000000000000, 99999999999999)


def add_new_book_input():
    return {
                "name": get_input_book_value("Podaj nazwe Ksiazki"),
                "isbn": generate_isbn(),
                "autor": {
                    "name": get_input_book_value("Podaj imie autora"),
                    "surrname": get_input_book_value("Podaj nazwisko autora")
                }
            }


def chose_menu():
    start = True
    while start:
        show_menu_list()
        chose = get_menu()
        if chose == 0:
            start = end_app()
        if chose == 1:
            book = add_new_book_input()
            add_book(book_list, book)
        if chose == 2:
            show_books(book_list)
        if chose == 3:
            if len(book_list) == 0:
                print("Lista nie ma książek. Nie mam czego usunąć")
            else:
                key = get_book_to_delete()
                delete_book(book_list, key)


if __name__ == "__main__":
    book_list = read()
    chose_menu()
    save(book_list)
