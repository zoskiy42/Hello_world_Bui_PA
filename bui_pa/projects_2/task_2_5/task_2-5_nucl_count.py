with open("count.txt", "w", encoding="utf-8") as ATGC:
    
    ATGC.write("=== Анализ последовательности ДНК ===\n")
    
    subsequence = input("Введите последовательность ДНК: ").upper()
    
    count_A = subsequence.count("A")
    count_T = subsequence.count("T")
    count_G = subsequence.count("G")
    count_C = subsequence.count("C")
    
    count_all = count_A + count_T + count_G + count_C
    one_procent = 100 /count_all 


    ATGC.write(f"\nПоследовательность в верхнем регистре: {subsequence}\n\n")
    ATGC.write("Подсчёт нуклеотидов:\n")
    ATGC.write(f"A: {count_A}\n")
    ATGC.write(f"T: {count_T}\n")
    ATGC.write(f"G: {count_G}\n")
    ATGC.write(f"C: {count_C}\n")
    ATGC.write(f"\nОбщая длина: {count_all}\n")
    ATGC.write("\nПроцентное содержание нуклеотидов:\n")
    ATGC.write(f"A (%): {one_procent * count_A:.3f}\n")
    ATGC.write(f"T (%): {one_procent * count_T:.3f}\n")
    ATGC.write(f"G (%): {one_procent * count_G:.3f}\n")
    ATGC.write(f"C (%): {one_procent * count_C:.3f}")
    print("Сохранено")