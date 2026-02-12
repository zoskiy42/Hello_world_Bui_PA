f = open("inventory.txt", "w", encoding="utf-8")
reagent = input()
quantity = int(input())

print(f'Реактив {reagent} поступил на склад в количестве {quantity} шт.', file=f)
f.close()