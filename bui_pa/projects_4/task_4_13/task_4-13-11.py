array = [2, 4, 6, 8, 10, 12]
index_sum = 0
count = 0
for i in range(len(array)):
    if i % 2 == 0: 
        index_sum += array[i]
        count += 1
print("Среднее элементов с четными индексами:", index_sum / count)