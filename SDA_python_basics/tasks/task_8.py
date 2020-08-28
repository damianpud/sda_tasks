def factorial(cyfra):
    i = 1
    iloczyn = 1
    if cyfra == 0:
        return 0
    else:
        while i <= cyfra:
            iloczyn = iloczyn*i
            i += 1
        return iloczyn


if __name__ == '__main__':
    number = int(input('Podaj liczbe: '))
    result = factorial(number)
    print(result)