import bisect


def function_sort(l):
    sorted_list = []
    for list_element in l:
        bisect.insort(sorted_list, list_element)
    return sorted_list


def insertion_sort(l):
    for index, list_element in enumerate(l):
        for i in reversed(range(1, index + 1)):
            if l[i - 1] > l[i]:
                temp = l[i]
                l[i] = l[i - 1]
                l[i - 1] = temp
            else:
                break


if __name__ == "__main__":
    my_list = [7, 4, 5, 2, 1, 9, 10, 3]
    insertion_sort(my_list)
    print(my_list)
