# Nornir

Nornir is a Python automation framework that is designed to automate network tasks, it's built on top of the popular libraries such as Netmiko and Napalm. It allows for parallel execution of tasks, and provides an easy-to-use inventory system to manage devices.

## Examples

Here are a few examples of how Nornir can be used to interact with Cisco routers:

* Creating an inventory: Nornir uses an inventory system to manage the devices. Here's an example of how to create an inventory of Cisco routers:

```
from nornir import InitNornir
from nornir.plugins.inventory import SimpleInventory

# Define the devices
devices = {
    "cisco_router1": {
        "hostname": "192.168.1.1",
        "username": "admin",
        "password": "password",
        "platform": "cisco_ios",
    },
    "cisco_router2": {
        "hostname": "192.168.1.2",
        "username": "admin",
        "password": "password",
        "platform": "cisco_ios",
    },
}

# Create the inventory
nr = InitNornir(inventory=SimpleInventory(hosts=devices))

```

* Running commands on a Cisco router: Once connected, Nornir can be used to run commands on a Cisco router. Here's an example of how to run the "show version" command on a router using Nornir:

```
from nornir import InitNornir
from nornir.plugins.tasks import networking

# Initialize Nornir
nr = InitNornir(inventory={'options': {'host_file': 'hosts.yaml'}})

# Run the command on the device
result = nr.run(networking.netmiko_send_command, command_string='show version')

# Print the output
print(result['cisco_router'].result)
```

* Configuring a Cisco router: Nornir can also be used to configure Cisco routers. Here's an example of how to configure an interface on a Cisco router using Nornir:

```
from nornir import InitNornir
from nornir.plugins.tasks import networking

# Initialize Nornir
nr = InitNornir(inventory={'options': {'host_file': 'hosts.yaml'}})

# Define the configuration commands
commands = [ 'interface FastEthernet0/1',
'description Configured by Nornir',
'ip address 192.168.1.10 255.255.255.0',
'no shutdown' ]
```

* Send the configuration commands to the device and Print the result

```
result = nr.run(networking.netmiko_send_config, config_commands=commands)
print(result['cisco_router'].result)
```

> Nornir provides a powerful and flexible way to automate network tasks across multiple devices. It allows you to define devices and their connection details in a single file, and it also provides a simple and consistent way to run commands and configure devices. 
It also allows to perform parallel execution, gather data and perform filtering, and more.




   

