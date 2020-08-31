def sum_up(number):
    wyn = 0
    for x in range(number + 1):
        wyn += x
    return wyn


if __name__ == '__main__':
    number = int(input('Podaj liczbe: '))
    result = sum_up(number)
    print(result)