operator_name = input("Введите имя оператора:")
pressure_value = input("Введите текущее значение давления (Па):")

with open("sensor_log.txt", "w", encoding="utf-8") as page:
    page.write(f"Имя оператора:\t\t\t {operator_name}\nТекущее значение давления (Па):\t {pressure_value}\n")
    print("\nДанные успешно сохранены в sensor_log.txt")