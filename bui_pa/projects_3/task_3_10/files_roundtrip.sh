#!/bin/bash

for i in {1..10}; do
    touch "test$i.txt"
    echo "test$i.txt"
done

echo "Файлы успешно созданы"

counter=10
while [ $counter -ge 1 ]; do
    rm "test$counter.txt"
    echo "Удалён test$counter.txt"
    let "counter -= 1"
done

echo "Все файлы удалены"
