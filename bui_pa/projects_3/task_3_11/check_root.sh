#!/bin/bash

check_root() {
    if [ "$EUID" -eq 0 ]; then
        echo "Запущено от root"
        return 0
    else
        echo "ОШИБКА: запустите от root"
        echo "UID: $EUID"
        exit 1
    fi
}

check_root
