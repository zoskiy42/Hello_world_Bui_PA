weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)

print(f"\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height}см\nВес:\t{weight}кг\nИндекс массы тела: {bmi:.2f}")