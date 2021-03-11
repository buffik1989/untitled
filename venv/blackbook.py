"""ip = [10, 10, 10, 1, 24]
mask = ("1" * ip[4]) + "0" * (32 - ip[4])
mask_bin0 = mask[0:8]
mask_bin1 = mask[8:16]
mask_bin2 = mask[16:24]
mask_bin3 = mask[24:32]
print(mask_bin0)
print(mask_bin1)
print(mask_bin2)
print(mask_bin3)
mask_int0 = int(mask_bin0, 2)
mask_int1 = int(mask_bin1, 2)
mask_int2 = int(mask_bin2, 2)
mask_int3 = int(mask_bin3, 2)
print(mask_int0)

int_ip = [2556, 255, 255, 0]
if len(int_ip) == 4:
    for n in int_ip:
        if n in range(256):  # Проверка на 4 числа и диапазон до 255
            print("cool")
            ip_correct = True
            continue
    else:
        print('Неправильный IP-адрес')

ЗАДАНИЕ 6.2b
ip = input("Введите адрес в формате 10.0.1.1: ")
int_ip = []
ip_list = []
ip_command = False
while True:
    ip_list.clear
    ip = input('Повторно введите IP-адрес: ')  # Повторый ввод IP
    try:
        ip_list = ip.split('.')         #Формирования списка чисел и проверка на правильность литералов
        for indx in ip_list:
            int_ip.append(int(indx))
            break
    except ValueError:
        print("Ошибка в литеральных символах")
        ip_list.clear
        ip = input('Повторно введите IP-адрес: ')  # Повторый ввод IP

print(int_ip)
    for n in int_ip:
        if n not in range(0, 256):  # Проверка на числа и диапазон до 255
            print("Ошибка в диапазоне")
            ip_list.clear
            ip = input('Повторно введите IP-адрес: ')  # Повторый ввод IP
            continue
        else:
            pass
    if len(int_ip) != 4:            # Проверка на 4 числа
        break
    else:
        print("Введите 4 числа")
        ip_list.clear()
        ip = input('Повторно введите IP-адрес: ')  # Повторый ввод IP
        continue

if int_ip[0] in range(1, 223):
    print('unicast')
elif int_ip[0] in range(224, 239):
    print('imultcast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('local broadcast')
else:
    print('unused')"""