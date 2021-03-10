# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите адрес в формате 10.0.1.1: ")
int_ip = []
ip_list = []
i = -1
ip_correct = False
while i < 4:
    if i != -1:
        ip = input("Введите пароль еще раз: ")
        int_ip.clear()
        ip_list.clear()
    i = 0
    try:
        ip_list = ip.split('.')
        for indx in ip_list:
            int_ip.append(int(indx))
        print(int_ip)
        if len(int_ip) == 4:
            for n in int_ip:
                if n in range(256):  #Проверка на 4 числа и диапазон до 255
                    i += 1
                else:
                    print("Ошибка в диапазоне")
                    break
        else:
            print('Введите 4 числа')
    except ValueError:
        print('Используйте только цифры и символ "." ')
    except IndexError:
        print('Используйте только цифры и символ "." ')

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