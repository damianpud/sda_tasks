import random
from time import perf_counter

x = list()


def random_list():
    random_numbers = []
    for _ in range(1000):
        random_numbers.append(random.randint(1, 10000))
    return random_numbers


def quick_sort(t, L, P):
    i = L
    j = P
    x = t[int((L + P) / 2)]
    while i < j:
        while t[i] < x:
            i = i + 1
        while t[j] > x:
            j = j - 1
        if i <= j:
            bufor = t[i]
            t[i] = t[j]
            t[j] = bufor
            i = i + 1
            j = j - 1
        if L < j:
            quick_sort(t, L, j)
        if i < P:
            quick_sort(t, i, P)
    return t


if __name__ == "__main__":
    list_1 = random_list()
    print(list_1)
    start = perf_counter()
    print(sorted(list_1))
    stop = perf_counter()
    print(stop - start)
    start = perf_counter()
    print(quick_sort(list_1, 0, len(list_1) - 1))
    stop = perf_counter()
    print(stop - start)
