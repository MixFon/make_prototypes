#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

def name_function(line):
    name = ""
    name = line[line.find("\t"):line.find("(")]
    name = name.lstrip(' \t*')
    name += ".c"
    return name

def write_prototyps(prototypes, name_files, head):
    try:
        out = open(head, "a")
        print("\nВ файл " + head + " добавленны следующие прототипы:")
        for i in range(len(name_files)):
            if i % 5 == 0:
                out.write("/*\n** File " + name_files[i] + "\n*/\n")
            print(prototypes[i])
            out.write(prototypes[i] + "\n")
        out.close()
    except IOError:
        print("Ошибка открытия файла!")
        exit(0)


def write_funtions(prototypes, name_files, head):
    try:
        print("\nСозданы следующие файлы:")
        for i in range(len(name_files)):
            if i % 5 == 0:
                print(name_files[i])
                out = open(name_files[i], "w")
                out.write("\n#include \"" + head + "\"\n\n")
            out.write(functions[i])
        out.close()
    except IOError:
        print("Ошибка открытия файла!")
        exit(0)

if len(sys.argv) != 2:
    print("Введите вторым аргументов название файла, в котором находите прототипы")
    exit()

prototypes = []
functions = []
name_files = []
func = ""
try:
    f = open(sys.argv[1], 'r')
    for line in f:
        func += line
        if line[0].isalpha():
            prototypes.append((line[:-1] + ";"))
            name_files.append(name_function(line)) 
        if line[0] == '}':
            functions.append(func)
            func = ""
    f.close()
except IOError:
    print("Неверное имя файла!")
    exit(0)

head = input("Введите имя файла .h\n")
write_prototyps(prototypes, name_files, head)
write_funtions(functions, name_files, head)
f.close()
