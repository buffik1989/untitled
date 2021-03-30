access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}

def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    for key, val in access_template.items():
        print(f'{key}, {intf_vlan_mapping[0]}, {intf_vlan_mapping[1]} {val}, {intf_vlan_mapping[2]}, {intf_vlan_mapping[3]}, {intf_vlan_mapping[4]}', end = ', ')
        print('{}, {}, {}'.format(*psecurity))

generate_access_config(access_mode_template, access_config, port_security_template)