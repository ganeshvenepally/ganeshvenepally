# Netmiko

Netmiko is a Python library built on top of Paramiko, which simplifies automating network device configuration and management tasks. It is designed to work with Cisco, Arista, Juniper, and other network vendors.

## Examples 

**Here are a few examples of how Netmiko can be used to interact with Cisco routers:** 

* Connecting to a Cisco router: Netmiko can be used to establish an SSH connection to a Cisco router. Here's an example of how to connect to a router using Netmiko:

```
from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

# Connect to the device
net_connect = ConnectHandler(**device)
```

* Running commands on a Cisco router: Once connected, Netmiko can be used to run commands on a Cisco router. Here's an example of how to run the "show version" command on a router:

```
output = net_connect.send_command("show version")
print(output)
```

* Configuring a Cisco router: Netmiko can also be used to configure Cisco routers. Here's an example of how to configure an interface on a Cisco router:

```
# Define the configuration commands
commands = [
    'interface FastEthernet0/1',
    'description Configured by Netmiko',
    'ip address 192.168.1.10 255.255.255.0',
    'no shutdown'
]

# Send the configuration commands to the device
net_connect.send_config_set(commands)
```
> Netmiko provides a simple and consistent interface to interact with network devices and automate tasks such as configuration management, backup, troubleshooting and more. It supports a wide range of network vendors and platforms, and it includes support for SSH, Telnet and serial connections.

