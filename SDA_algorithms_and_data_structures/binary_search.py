def binary_search(list_numbers, value):
    l = 0
    p = len(list_numbers) - 1
    if l > p:
        return "empty list"
    while True:
        s = int((l + p) / 2)
        if list_numbers[s] == value:
            return f"Number {value} is on index {s}"
        if list_numbers[s] < value:
            l = s + 1
        else:
            p = s - 1


if __name__ == "__main__":
    list_1 = [element + 1 for element in range(20)]
    print(binary_search(list_1, 14))
