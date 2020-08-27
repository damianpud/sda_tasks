""" 2. Napisz funkcję perfect_squares, przyjmującą liczbę quantity. Jej zadaniem jest znalezienie tzw. "idealnych kwadratów", czyli liczb,
które mogą powstać przez podniesienie liczby całkowitej do kwadratu (przykładami "idealnego kwadratu" są liczby 1=1*1, 4=2*2, 9=3*3,
16=4*4 itd., ale np. 12 nie jest idealnym kwadratem). Zdefiniuj w tym celu funkcję is_perfect_square, sprawdzającą czy dana liczba
jest idealnym kwadratem."""


def perfect_squares(quantity):
    list2 = []
    numb = 1
    while (True):
        result = is_perfect_square(numb)
        if result == True:
            list2.append(numb)
        numb += 1
        if len(list2) == quantity:
            return list2


def is_perfect_square(number):
    for i in range(number - 1):
        if (i + 2) < number:
            result = number / (i + 2)
            if result ** 2 == number:
                return True
    return False


if __name__ == "__main__":
    print(perfect_squares(10))
    print(is_perfect_square(15))