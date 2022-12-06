def gcd(a, b):
    print(a, b)

    # base case
    if b == 0:
        return a

    return gcd(b, a % b)


