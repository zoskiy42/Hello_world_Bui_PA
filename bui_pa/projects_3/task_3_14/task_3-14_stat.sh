#!/bin/bash

awk '{sum += $2} END {print "Сумма оценок:", sum}' students.txt

awk '{sum += $2; n++} END {print "Средняя оценка:", sum/n}' students.txt

awk 'NR==1 {max=$2} $2>max {max=$2} END {print "Максимальная оценка:", max}' students.txt
