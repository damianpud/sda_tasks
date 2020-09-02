list = ('Wyjscie', 'Dodaj', 'Odejmij', 'Pomnoz', 'Podziel')


def dodawanie(x, y):
    return x + y


def odejmowanie(x, y):
    return x - y


def mnozenie(x, y):
    return x * y


def dzielenie(x, y):
    return x / y


def wartosc_x():
    return int(input('Podaj pierwszą liczbe: '))


def wartosc_y():
    return int(input('Podaj druga liczbe: '))


def get_input_int(text):
    try:
        return int(input(text))
    except Exception:
        print('error')


def get_input_float(text):
    try:
        return float(input(text))
    except Exception:
        print('error')
    return


def kalkulator():
    while True:
        print('Hello')
        for element in list:
            print(list.index(element) + 1, element)

        wybor = int(input('Wybierz opcje z menu: '))

        if wybor == 1:
            print('Bye bye')
            break

        elif wybor == 2:
            print('wynik dodawanie:', dodawanie(wartosc_x(), wartosc_y()))

        elif wybor == 3:
            print('wynik odejmowania:', odejmowanie(wartosc_x(), wartosc_y()))

        elif wybor == 4:
            print('wynik mnozenia:', mnozenie(wartosc_x(), wartosc_y()))

        elif wybor == 5:
            print('wynik dzielenia:', dzielenie(wartosc_x(), wartosc_y()))

        else:
            print('Nie dokonales wyboru')


if __name__ == "__main__":
    kalkulator()