# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

com1 = command1[command1.find('1,2,3')::]
print(com1)
com2 = command2[command2.find('1,3,8')::]
print(com2)
com1 = com1.replace(',',' ')
com1 = com1.split()
print(com1)
com2 = com2.replace(',', ' ')
com2 = com2.split()
print(com2)