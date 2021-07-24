#!/usr/bin/python3
# Данная программа заменяет 4 пробела на одит таб и убирает пробелы в конце сьроки.
# Имя файла передается первым аргуменом при запуске программы.
# В результате создается новый файл с приставкой new_ в той же папке.
# Запускать скрипт необходмо в той же папке, что и исправляемый файл.
import sys


if len(sys.argv) != 2:
    print("Первый папраметр имя файла в котором нужно заменить пробелы на табы")
    exit(-1)

file_name = sys.argv[1]

try:
    file = open(file_name, 'r')
    data = ""
    for line in file:
        data += line.replace("    ", "\t").strip(" ")

    name_new_file = "new_" + file_name
    new_file = open(name_new_file, "w")
    new_file.write(data)
    print("Создан новый файл:", name_new_file)
    file.close()
except IOError:
    print("Неверное имя файла!")
    exit(0)
