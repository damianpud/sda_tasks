import random
import json

file_name = "ranking.txt"

menu = ("Graj", "Pokaz ranking", "Wyjscie")
difficulty_level = ("Latwy", "Sredni", "Trudny")


def file_exist():
    try:
        f = open(file_name, "r")
        f.close()
        print("Plik juz istnial")
        return True
    except Exception:
        open(file_name, "x")
        print("Plik nie istnial. Stworzylismy nowy")
        return False


def read():
    print("Read from file")
    if file_exist():
        try:
            f = open(file_name, "r")
            data = f.read()
            f.close()
            print("Udalo sie zaladowac dane")
            return json.loads(data)
        except Exception:
            print("Nie udalo sie wczytac danych z pliku")
            return {}
    print("Pierwsze uruchomienie programu - tworzymy puste dane")
    return {}


def save(data={}):
    print("Save to file")
    file_exist()
    try:
        f = open(file_name, "w")
        f.write(json.dumps(data))
        print("Udalo sie zapisac dane do pliku")
    except Exception:
        print("Nie udalo sie zapisac danych do pliku")


def end_app():
    print("Bye bye")
    return False


def random_number(level):
    return random.randint(0, level)


def show_menu_list(list):
    for index in range(len(list)):
        print(f"{index + 1}. {list[index]}")


def game(number):
    step = 1

    while(True):
        try:
            player_number = int(input("Odgadnij wylosowana liczbe: "))
            if number < player_number:
                print("Podana liczba jest mniejsza od ukrytej liczby.")
            elif number > player_number:
                print("Podana liczba jest wieksza od ukrytej liczby.")
            elif number == player_number:
                print("Gratuluje podales prawidlowa licze !!!")
                print(f"Odgadles liczbe w {step} krokach.")
                print("\n")
                return step
            step += 1
        except Exception:
            print("Podales bledna wartosc")


def dict_rank(add_dict, key, value):
    add_dict[key] = value
    del_items(add_dict)


def sort_rank(rank_dict):
    sort_list = []
    sort_dict = {}
    index = 0
    for key, value in rank_dict.items():
        sort_list.append(value)
    sort_list.sort()
    for i in range(len(sort_list)):
        for key, value in rank_dict.items():
                if sort_list[index] == value:
                    sort_dict[key] = value
        index += 1
    return sort_dict


def choice_difficulty_level():
    try:
        return int(input("Wybierz poziom trudnosci: "))
    except Exception:
        print("Sproboj ponownie")


def choice_menu():
    try:
        return int(input("Wybierz z menu: "))
    except Exception:
        print("Sproboj ponownie")


def show_rank(ranking_dict):
    x = 0
    index_dict = [index + 1 for index in range(len(sort_rank(ranking_dict)))]
    for key, value in sort_rank(ranking_dict).items():
        print(f"{index_dict[x]}. {key}: {value}")
        x += 1


def del_items(dict_del):
    sort_list = []
    for key, value in dict_del.items():
        sort_list.append(value)
    sort_list.sort()
    if len(dict_del) > 10:
        for key, value in dict_del.items():
            if sort_list[-1] == value:
                dict_del.pop(key)
                return dict_del


def play_game():
    start = True

    while start:
        show_menu_list(menu)
        choice = choice_menu()
        print("\n")
        if choice == 1:
            show_menu_list(difficulty_level)
            level = choice_difficulty_level()
            name = input("Podaj imie: ")
            print("\n")
            if level == 1:
                number = random_number(10)
                result = game(number)
                dict_rank(rank_dict_low, name, result)
            elif level == 2:
                number = random_number(100)
                result = game(number)
                dict_rank(rank_dict_medium, name, result)
            elif level == 3:
                number = random_number(1000)
                result = game(number)
                dict_rank(rank_dict_hard, name, result)
        elif choice == 2:
            print("Ranking dla latwego poziomu trudnosci:\n")
            show_rank(rank_dict_low)
            print("\n")
            print("Ranking dla średniego poziomu trudnosci:\n")
            show_rank(rank_dict_medium)
            print("\n")
            print("Ranking dla trudnego poziomu trudnosci:\n")
            show_rank(rank_dict_hard)
            print("\n")
        elif choice == 3:
            start = end_app()


if __name__ == "__main__":
    ranking = list(read())
    rank_dict_low, rank_dict_medium, rank_dict_hard = ranking[0], ranking[1], ranking[2]
    play_game()
    ranking = [rank_dict_low, rank_dict_medium, rank_dict_hard]
    save(ranking)