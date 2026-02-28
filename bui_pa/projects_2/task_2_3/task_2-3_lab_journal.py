name = input("ФИО: ")
data = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

conclusion_0 = conclusion.split()
min =("+" + "-" * 55 + "+")

with open("journal.txt", "w", encoding="utf-8") as page:
    page.write(min)
    page.write(f"\n| Электронный лабораторный журнал\t\t\t|\n")
    page.write(min)
    page.write(f"\n| ФИО исследователя\t: {name}\t\t|\n")
    page.write(f"| Дата\t\t\t: {data}\t\t\t|\n")
    page.write(f"| Эксперимент\t\t: {experiment}\t|\n")
    page.write(min)
    page.write(f"\n| Вывод:\t\t\t\t\t\t|\n")
#    for word in conclusion_0[0:10]:
#        page.write(f"| {word} \t\t|\n")
    page.write(f"| {conclusion_0[0:5]}|\n")
    page.write(f"| {conclusion_0[5:9]}|\n")
    page.write(f"| {conclusion_0[9:10]}\t\t\t\t\t\t|\n")
    page.write(min)
# В ходе эксперимента выявлены нарушения долговременной памяти у экспериментальной группы животных.