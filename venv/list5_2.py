# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input("Введите IP в формате: 10.1.1.0/24: ")
ip = ip.replace('.', ' ')
ip = ip.replace('/',' ')
ip = ip.split()
print("-" * 30)


print(f'''Network:\n{ip[0]:<8} {ip[1]:<8} {ip[2]:<8} {ip[3]:<8}''')
print(f'''{int(ip[0]):08b} {int(ip[1]):08b} {int(ip[2]):08b} {int(ip[3]):08b}''')
ip_int = int(ip[4])
#print(ip_int)
mask = str(("1" * ip_int) + "0" * (32 - ip_int))
#print(mask)
mask_bin0 = mask[0:8]
mask_bin1 = mask[8:16]
mask_bin2 = mask[16:24]
mask_bin3 = mask[24:32]

'''print(mask_bin0)
print(mask_bin1)
print(mask_bin2)
print(mask_bin3)'''

mask_int0 = int(mask_bin0, 2)
mask_int1 = int(mask_bin1, 2)
mask_int2 = int(mask_bin2, 2)
mask_int3 = int(mask_bin3, 2)

print(f'''Mask:\n/{ip[4]}''')
print(f'''{mask_int0:<8} {mask_int1:<8} {mask_int2:<8} {mask_int3:<8}''')
print(f'''{mask_bin0:<8} {mask_bin1:<8} {mask_bin2:<8} {mask_bin3:<8}''')
