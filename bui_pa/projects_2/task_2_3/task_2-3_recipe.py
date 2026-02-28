environment = input("Введите название питательной среды:")
agar_concentration = input("Введите концентрацию агара (%):")
sterilization_temperature = input("Введите температуру стерилизации (°C):")

with open("recipe.txt", "w", encoding="utf-8") as page:
    page.write(f"Название питательной среды: {environment}\nКонцентрацию агара (%): {agar_concentration}\nТемпературу стерилизации (°C): {sterilization_temperature}\n")
    print(f"\nФайл 'recipe.txt' успешно сформирован!")