n = int(input("Сколько введете? "))
max = float(input("1-е число: "))

for i in range(2, n + 1):
    cur = float(input(f"{i}-е число: "))
    if cur > max:
        max = cur

print("Максимум: ", max)