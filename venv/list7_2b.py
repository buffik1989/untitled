# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt') as f, open('config_sw1_cleared.txt', 'w') as res:
    for line in f:
        for val in ignore:
            if val in line:
                break
            else:
                if ignore.index(val) + 1 == len(ignore):
                    res.write(line)

with open('config_sw1_cleared.txt') as f:
    for line in f:
        print(line.rstrip())