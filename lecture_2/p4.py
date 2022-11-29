def sum_of_digits(n):
    # base case
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


def sum_of_digits(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
