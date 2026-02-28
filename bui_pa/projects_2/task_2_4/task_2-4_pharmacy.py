capsule = int(input("Введите общее количество произведенных капсул: "))
package = int(input("Введите количество капсул в одной упаковке: "))

packages = capsule // package
capsules = capsule % package

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{packages}\nОстаток капсул:\t\t{capsules}")