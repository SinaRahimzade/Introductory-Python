def print_star_pattern():
    for i in range(1, 10, 2):
        print(" " * ((9 - i) // 2) + "*" * i)
    for i in range(7, 0, -2):
        print(" " * ((9 - i) // 2) + "*" * i)


def print_star_pattern_2():
    print(4 * " " + "*")
    for i in range(2, 6):
        print(" " * (5 - i) + "*" + " " * (2 * i - 3) + "*")
    print("*" * 9)


print_star_pattern_2()
