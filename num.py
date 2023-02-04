d1={num:num+num for num in range(10)}
print(d1)
print()
print(type(d1))
print()
for x1 in d1.keys ():
    print(x1)
    print()
    for y1 in d1.values ():
        print(y1)
        print()
        for x1,y1 in d1.items ():
            print("x1,...,y1")
            print()