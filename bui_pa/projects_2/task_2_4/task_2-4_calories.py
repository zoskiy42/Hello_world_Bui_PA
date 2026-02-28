proteins = float(input("Массу белков в продукте (г):"))
fats = float(input("Массу жиров в продукте (г):"))
carbohydrates = float(input("Массу углеводов в продукте (г):"))

calories= (proteins*4)+(fats*9)+(carbohydrates*4)

print(f"Калорийность: {calories}")