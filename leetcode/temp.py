l = [1, 2, 3, 4, 5]

for i in range(5):
    for element in enumerate(l, start=i):
        print(element)