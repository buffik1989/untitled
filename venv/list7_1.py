 # -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('ospf.txt', 'r') as f, open('result.txt', 'w') as dest:
    for line in f:
        c = ""
        b = line.replace(',',' ')
        a = b.split()
        res = f"Protocol:{a[0]:>15}SPF\nPrefix:{a[1]:>28}\nAD/Metric:{a[2]:>21}\nNext-Hop:{a[4]:>23}\nLast update:{a[5]:>16}\nOutbound Interface:{a[6]:>19}\n" + ("-"*30)
        dest.write(res)

with open('result.txt') as q:
    for line in q:
        print(line)
