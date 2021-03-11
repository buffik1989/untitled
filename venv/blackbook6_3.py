trunk_template = [
    'switchport trunk allowed vlan add', 'switchport trunk allowed vlan remove',
    'switchport trunk allowed vlan'
    ]



trunk = {
        '0/1': ['add', '10', '20', '30', '30'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for key, val in trunk.items():
    print('interface FastEthernet ' + key)
    i = 1
    vals = len(val)
    a = ""
    while vals > i:    #Отвечает за подстановку вланов из листа trunk
        if vals == 2 or vals - 1 == i:
            a += val[i] + "."
        else:
            a += val[i] + ", "
        i += 1
    if val[0] == 'add':
        print("{} {}".format(trunk_template[0], a))
        print("-" * 30)
    elif val[0] == 'only':
        print('{} {}'.format(trunk_template[2], a))
        print("-" * 30)
    elif val[0] == 'del':
        print('{} {}'.format(trunk_template[1], a))
        print("-" * 30)
    else:
        print("Ooops")