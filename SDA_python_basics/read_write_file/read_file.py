def read_demo_file():
    f = open("demo_file.txt", "r")
    print(f.read())
    f.close()


def read_py_file():
    f = open("hamming.py", "r")
    print(f.read())
    f.close()


if __name__ == "__main__":
    try:
        read_py_file()
    except Exception:
        print("File not exist")