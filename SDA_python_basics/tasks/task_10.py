import json
file_name = "save_file.txt"


def file_exist():
    try:
        f = open(file_name, "r")
        f.close()
        print("Plik juz istnial")
        return True
    except Exception:
        open(file_name, "x")
        print("Plik nie istnial. Stworzylismy nowy")
        return True


def read():
    print("Read from file")
    if file_exist():
        try:
            f = open(file_name, "r")
            data = f.read()
            # print(data)
            f.close()
            print("Udalo sie zaladowac dane")
            return json.loads(data)
        except Exception:
            print("Nie udalo sie wczytac danych z pliku")
            return []
    return []


def save(data = []):
    print("Save to file")
    file_exist()
    try:
        f = open(file_name, "w")
        f.write(json.dumps(data))
        f.close()
        print("Udalo sie zapisac dane do pliku")
    except Exception:
        print("Nie udalo sie zapisac danych do pliku")


def add():
    x = {}
    key = input("Wprowadź login: ")
    value = input("Wprowadź hasło: ")
    x[key] = value
    return x


def add_data(lists):
    lists.append(add())


def check_login(lists):
    login = input("podaj login: ")
    password = input("podaj hasło: ")
    for ele in lists:
        for key, val in ele.items():
            if key == login and val == password:
                return True


def show_menu_list(list):
    for index in range(len(list)):
        print(f"{index + 1}. {list[index]}")


def try_choice():
    try:
        return int(input("Wybierz z listy: "))
    except Exception:
        print("Sproboj jeszcze raz. \n")


def start():
    menu_list = ("Zaloguj się", "Zarejstruj się", "Wyjscie")
    start = True
    while start:
        show_menu_list(menu_list)
        choice = try_choice()
        if choice == 1:
            login_haslo = list(read())
            log = check_login(login_haslo)
            if log == True:
                print("Udało Ci się zalogować")
            else:
                print("Nie udało Ci sie zalogować")
            save(login_haslo)
        elif choice == 2:
            login_haslo = list(read())
            add_data(login_haslo)
            save(login_haslo)
        elif choice == 3:
            start = False
            print("Bye bye")


if __name__ == "__main__":
    start()