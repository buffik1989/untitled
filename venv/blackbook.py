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
print(mask_int0)"""

int_ip = [2556, 255, 255, 0]
if len(int_ip) == 4:
    for n in int_ip:
        if n in range(256):  # Проверка на 4 числа и диапазон до 255
            print("cool")
            """ip_correct = True
            continue"""
    else:
        print('Неправильный IP-адрес')