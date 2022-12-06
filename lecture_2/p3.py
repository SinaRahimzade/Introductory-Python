def find_num_in_range(n, m):
    for i in range(n, m + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


inp = input()
n = int(inp.split(" ")[0])
m = int(inp.split(" ")[1])
find_num_in_range(n, m)