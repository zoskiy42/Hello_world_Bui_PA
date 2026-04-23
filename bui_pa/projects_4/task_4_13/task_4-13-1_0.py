a = float(input("Число 1: "))
b = float(input("Число 2: "))
c = float(input("Число 3: "))
d = float(input("Число 4: "))

if a < b:
    min_1 = a
else:
    min_1 = b
if c < d:
    min_2 = c
else:
    min_2 = d
    if min_1 < min_2:
        min = min_1
    else:
        min = min_2
        print(min)