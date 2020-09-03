def write_to_file():
    f = open("demo_file.txt", "w")
    f.write("Now the file has a content! \n")
    f.close()


def add_to_file():
    f = open("demo_file.txt", "a")
    f.write("Now the file has new content! \n")
    f.close()


if __name__ == "__main__":
    write_to_file()
    add_to_file()


