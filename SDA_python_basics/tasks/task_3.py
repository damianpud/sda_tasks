""" 3. Napisz funkcję rotate_list, która przyjmować będzie jako argument listę processed_list oraz skok step. Zadaniem funkcji
jest "rotowanie" listy, tzn. przesunięcie jej elementów o skok step (przykładowo, dla listy [1, 2, 3, 4, 5] i skoku 3 funkcja
powinna zwrócić listę [4, 5, 1, 2, 3], a dla listy [8, 7, 6, 5, 4, 3, 2] i skoku 2 funkcja powinna zwrócić
listę [6, 5, 4, 3, 2, 8, 7]. Spróbuj umożliwić podawanie ujemnego skoku (wtedy funkcja powinna przesuwać liczby w drugą stronę)."""


def rotate_list(processed_list, step):
    if step < 0:
        for i in range(- step):
            processed_list.insert(0, processed_list[-1])
            del processed_list[-1]
    for i in range(step):
        processed_list.append(processed_list[0])
        del processed_list[0]
    return processed_list


if __name__ == "__main__":
    print(rotate_list([8, 7, 6, 5, 4, 3, 2], 4))
