""" 1. Napisz funkcję prime_numbers, która przyjmować będzie liczbę quantity. Jej zadaniem jest wyświetlenie quantity liczb pierwszych.
Liczba pierwsza to taka liczba, która jest podzielna tylko przez 1 oraz samą siebie. Pomocniczo, opracuj funkcję is_prime,
przyjmującą liczbę number, która będzie sprawdzała, czy dana liczba jest liczbą pierwszą."""


def is_prime(number):
    list1 = []
    for i in range(number + 1):
        if (i + 1) < number + 1:
            result = number % (i + 1) == 0
            if result:
                list1.append(result)
    if len(list1) == 2:
        return True
    return False


def prime_numbers(quantity):
    list2 = []
    numb = 1
    while True:
        result = is_prime(numb)
        if result:
            list2.append(numb)
        numb += 1
        if len(list2) == quantity:
            return list2


if __name__ == "__main__":
    print(prime_numbers(100))
