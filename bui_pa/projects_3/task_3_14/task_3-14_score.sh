#!/bin/bash

echo "Оценка выше 80"
awk '$2 > 80 {print $1, $2}' students.txt

echo -e "\nОценка ниже 70"
awk '$2 < 70 {print $1, $2}' students.txt

echo -e "\nПервая строка файла"
awk 'NR == 1' students.txt
