import json
file_name = "book_data.txt"


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
            f.close()
            print("Udalo sie zaladowac dane")
            return json.loads(data)
        except Exception:
            print("Nie udalo sie wczytac danych z pliku")
            return []
    return []


def save(data={}):
    print("Save to file")
    file_exist()
    try:
        f = open(file_name, "w")
        f.write(json.dumps(data))
        f.close()
        print("Udalo sie zapisac dane do pliku")
    except Exception:
        print("Nie udalo sie zapisac danych do pliku")


if __name__ == '__main__':
    pass

