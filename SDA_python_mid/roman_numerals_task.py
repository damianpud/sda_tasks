import re


class Error(Exception):
    pass


class StringError(Error):
    def __init__(self, error):
        super().__init__(error)


numbers_dict = {'I': 1,
                'IV': 4,
                'V': 5,
                'IX': 9,
                'X': 10,
                'XL': 40,
                'L': 50,
                'XC': 90,
                'C': 100,
                'CD': 400,
                'D': 500,
                'CM': 900,
                'M': 1000
                }


def find_different_numbers(number: str):
    elements = []
    for el in number:
        elements.append(el)
        if el not in numbers_dict:
            raise StringError(f"You have added wrong string, '{number}' is not roman numeral.")
    if len(elements) == 0:
        raise StringError('You have added empty string.')
    else:
        return re.findall('I[VX]{1}|I|V|X[LC]{1}|X|L|C[DM]{1}|C|D|M', number)


def calculate(numbers_list):
    amount = 0
    for element in numbers_list:
        amount += numbers_dict[element]
    return amount


if __name__=="__main__":
    try:
        number = 'MMMDCCCLXXXIV'
        numbers_list = find_different_numbers(number)
        print(numbers_list)
        print(calculate(numbers_list))
    except TypeError:
        print(f"Error: 'int' object '{number}' is not iterable.")
    except StringError as e:
        print(f"Error: {e}")