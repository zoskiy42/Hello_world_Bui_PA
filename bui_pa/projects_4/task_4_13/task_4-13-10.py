array = [10, 20, 30, 40, 50, 60] 
index_sum = 0
for i in range(len(array)):
    if i % 2 != 0:
        index_sum += array[i]
print("Сумма элементов с нечетными индексами:", index_sum)