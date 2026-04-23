n = float(input("Введите N: "))
sum = 0

for i in range(1, n + 1):
    sum = sum + i

print(f"Сумма первых {n} чисел = {sum}")