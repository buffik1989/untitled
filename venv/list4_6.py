# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'OSPF        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
new_osp = ospf_route.lstrip("        ")
print(new_osp)
new = new_osp.replace(',', '')
print(new)
command = new.split()
print(command)
command.remove('via')
print(command)
print(f'''Protocol:              {command[0]}
Prefix:                {command[1]}
AD/Metric:             {command[2]}
Next-Hop:              {command[3]}
Last update:           {command[4]}
Outbound Interface     {command[5]}''')#.format({command[0]},{command[1]},{command[2]},{command[3]},{command[4]})
