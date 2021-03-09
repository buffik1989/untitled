# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'imultcast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Введите адрес в формате 10.0.1.1: ")
ip_list = ip.split('.')
int_ip = []
for indx in ip_list:
    int_ip.append(int(indx))
print(int_ip)
if int_ip[0] in range (1, 223):
    print('unicast')
elif int_ip[0] in range (224, 239):
    print('imultcast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('local broadcast')
else:
    print('unused')
