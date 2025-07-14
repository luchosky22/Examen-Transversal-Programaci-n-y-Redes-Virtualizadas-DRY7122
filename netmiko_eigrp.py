from netmiko import ConnectHandler


router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco",
}


eigrp_config = [
    "router eigrp SDN",
    "address-family ipv4 unicast autonomous-system 100",
    "network 192.168.56.0 0.0.0.255",
    "passive-interface default",
    "no passive-interface GigabitEthernet1",
    "exit-address-family"
]


net_connect = ConnectHandler(**router)

print("🔧 Enviando configuración EIGRP...")
output = net_connect.send_config_set(eigrp_config)
print(output)

print("📄 Resultado: show run | section eigrp")
print(net_connect.send_command("show run | section eigrp"))

print("📄 Resultado: show ip interface brief")
print(net_connect.send_command("show ip interface brief"))

print("📄 Resultado: show running-config")
print(net_connect.send_command("show running-config"))

print("📄 Resultado: show version")
print(net_connect.send_command("show version"))

net_connect.disconnect()
