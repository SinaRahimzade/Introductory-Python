inp = '1,2,3,4,5,6,7'
lst = inp.split(',')
lst = [int(i) for i in lst]

b = []
for i in lst:
    b.append(int(i))

print(lst)

