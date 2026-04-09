#!/bin/bash

read -p "Введите массу (кг): " readonly WEIGHT
read -p "Введите рост (м): " readonly HEIGHT

BMI=$((WEIGHT / (HEIGHT * HEIGHT)))

echo "Ваш ИМТ: $BMI"
