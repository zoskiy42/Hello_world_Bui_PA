files = ["seq1", "seq2", "seq3", "seq4"]
data = input()
with open("lab_log.txt", "w", encoding="utf-8") as file:
    file.write("Запись в журнале\n")

    for name in files:
        new_name = name + ".fasta " + data
        file.write(f"{new_name}\n")