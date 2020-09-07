import json


file_name = "name.txt"


def read_file():
    try:
        f = open("logins.py", "r")
        data = f.read()
        f.close()

    except Exception:
        return "file open error"
    else:
        return data


def write_to_file():
    try:
        f = open(file_name, "a")
        f.write("Woops! I have deleted the content!\n")
        f.close()
    except Exception:
        return "file open error"


def write_hello_py_file():
    python_data = 'def my_func():'
    python_data1 = '    x = 15'
    python_data2 = '    print(f"Hello World {x}")'
    python_data3 = 'my_func()'
    try:
        f = open("hello.py", "w")
        f.write(f"{python_data}\n")
        f.write(f"{python_data1}\n")
        f.write(f"{python_data2}\n")
        f.write(f"{python_data3}\n")
        f.close()
    except Exception:
        return "file open error"


if __name__ == "__main__":
    write_hello_py_file()
    json.dump()
