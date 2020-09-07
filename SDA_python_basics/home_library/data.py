def end_app():
    print("exit")
    return False


def add_book(book_list, book):
    print("add book")
    counter = len(book_list)
    key_name = "book{}".format(counter)
    book_list[key_name] = book
    print(f"Successfully added book \"{book['name']}\"")


def show_books(book_list):
    print("show book \n")
    for key, value in book_list.items():
        print("Key:", key)
        for elem in value:
            if elem == "autor":
                print("Autor:", value[elem]["name"], value[elem]["surrname"])
                print("\n")
            else:
                print(elem, ":", value[elem])


def delete_book(book_list, key):
    print("delete book")
    for k in book_list:
        if k == key:
            print(f"Successfully deleted book \"{book_list[k]['name']}\"")
            book_list[k] = {}
            break


first_list = {
            "book1": {"name": "ddd", "isbn": 222, "autor": { "name": "eee", "surrname": "zzz"}},
            "book2": {"name": "aaa", "isbn": 111, "autor": { "name": "ddd", "surrname": "xxx"}},
            "book3": {"name": "ccc", "isbn": 444, "autor": { "name": "ggg", "surrname": "yyy"}},
            "book4": {"name": "bbb", "isbn": 333, "autor": { "name": "fff", "surrname": "www"}}
            }


def show_books_sec(book_list):
    print("show book \n")
    for key, value in book_list.items():
        print("Key:", key)
        for elem in value:
            if elem == "autor":
                print("Autor:", value[elem]["name"], value[elem]["surrname"])
                print("\n")
            else:
                print(elem, ":", value[elem])


def sort_dict(book_list):
    sort_list = []
    sort_dict = {}
    index = 0
    char = ("name", "isbn", "autor")

    while True:
        choice = menu_sort()

        if choice == 2:
            for key, value in book_list.items():
                for elem in value:
                    if elem == char[choice]:
                        sort_list.append(value[elem]["surrname"])
            sort_list.sort()
            for i in range(len(sort_list)):
                for key, value in book_list.items():
                    for elem in value:
                        if sort_list[index] == value["autor"]["surrname"]:
                            sort_dict[key] = value
                index += 1
            return sort_dict

        else:
            for key, value in book_list.items():
                for elem in value:
                    if elem == char[choice]:
                        sort_list.append(value[elem])
            sort_list.sort()
            for i in range(len(sort_list)):
                for key, value in book_list.items():
                    for elem in value:
                        if sort_list[index] == value[char[choice]]:
                            sort_dict[key] = value
                index += 1
            return sort_dict


def menu_sort():
    list_choice = ("tytul", "isbn", "autor")
    for index in range(len(list_choice)):
        print(f"{index}. {list_choice[index]}")
    return int(input("Jak chcesz posortowac liste: "))


if __name__ == "__main__":
    while True:
        x = sort_dict(first_list)
        show_books(x)

