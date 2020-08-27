def diamond(x):
    this_list = []
    z = 1
    space = " "
    for i in range(x):
        y = x - z
        this_list.insert(0, f"{(x - y) * space}/{y * (2 * space)}\ ")
        this_list.append(f"{(x - y) * space}\{y * (2 * space)}/")
        z += 1
    for elem in this_list:
        print(elem)


if __name__ == "__main__":
    diamond(20)
