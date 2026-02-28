phenotype_patient = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()
phenotype_donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()

if phenotype_patient == "I":
    print("Группа крови пациента: 0 (I)")
elif phenotype_patient == "II":
    print("Группа крови пациента: A (II)")
elif phenotype_patient == "III":
    print("Группа крови пациента: B (III)")
elif phenotype_patient == "IV":
    print("Группа крови пациента: AB (IV)")
else:
    print("Такой группы крови не существует")
if phenotype_patient == phenotype_donor or phenotype_donor == "I":
    print("\nПодходящий донор")
else:
    print(f"\nНе подходит для переливания")