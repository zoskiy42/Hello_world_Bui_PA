n = int(input("N: "))
F = 1
for i in range(1, n + 1):
    F *= i
print(f"Факториал {n} =", F)