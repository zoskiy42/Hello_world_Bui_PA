#!/bin/bash

# Присваивание
CURRENT_YEAR=2026
read -n 4 -p "Введите год вашего рожления: " BIRTH_YEAR

# Вычисление (Арифметика)
AGE=$((CURRENT_YEAR - BIRTH_YEAR))

# Вывод с интерполяцией
echo "Текущий год: $CURRENT_YEAR"
echo "Ваш примерный возраст: $AGE"
