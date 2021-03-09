# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = input("Введите адрес в формате 10.0.1.1: ")

int_ip = []
try:
    ip_list = ip.split('.')
    for indx in ip_list:
        int_ip.append(int(indx))
    if len(int_ip) == 4:
        if int_ip[0] in range(1, 223):
            print('unicast')
        elif int_ip[0] in range(224, 239):
            print('imultcast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('local broadcast')
        else:
            print('unused')
except ValueError:
    print('Неправильный IP-адрес')

"""if int_ip[0] in range (1, 223):
    print('unicast')
elif int_ip[0] in range (224, 239):
    print('imultcast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('local broadcast')
else:
    print('unused')"""