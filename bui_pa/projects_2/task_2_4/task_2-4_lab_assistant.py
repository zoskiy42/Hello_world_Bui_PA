volume = float(input("Введите общий объём раствора (мл): "))
salt_mass = float(input("Введите массу соли (%): "))

formula_salt_mass = volume * (salt_mass * 0.01)
water_volume = volume - formula_salt_mass
min = "-" * 23

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n{min}\n")
    file.write(f"Общий объем:\t{volume} мл\nМасса соли:\t{formula_salt_mass:.2f} г\nОбъем воды:\t{water_volume} мл")