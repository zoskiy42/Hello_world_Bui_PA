array = [1, 2, 3, 4, 5, 6]
nech_sum = 0
for x in array:
    if x % 2 != 0:
        nech_sum += x
print("Сумма нечетных элементов:", nech_sum)