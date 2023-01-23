# Paramiko

Paramiko is a Python library that provides an SSH2 protocol implementation for secure and automated access to network devices such as routers and switches. It allows you to establish an SSH connection to a network device and execute commands or transfer files.

## Examples 
**Here are a few examples of how you can use paramiko to automate tasks on Cisco routers:**

* Connecting to a Cisco router: Paramiko can be used to establish an SSH connection to a Cisco router. Here's an example of how to connect to a router using Paramiko:


```
import paramiko

# Create a new SSH client
client = paramiko.SSHClient()

# Add the Cisco router's IP address and username/password to connect
client.connect('192.168.1.1', username='admin', password='password')

```

* Running commands on a Cisco router: Once connected, Paramiko can be used to run commands on a Cisco router. Here's an example of how to run the "show version" command on a router:

```
# Open an SSH channel
channel = client.invoke_shell()

# Send the command to the router
channel.send('show version\n')

# Receive the output from the router
output = channel.recv(9999)
print(output.decode())
```

* Transferring files to/from a Cisco router: Paramiko can also be used to transfer files to and from a Cisco router. Here's an example of how to transfer a file to a Cisco router:

```
# Open an SFTP session
sftp = client.open_sftp()

# Transfer the file to the router
sftp.put('local_file.txt', 'remote_file.txt')
```

> These are just a few examples of the many ways that Paramiko can be used to interact with Cisco routers. With Paramiko, you can automate tasks such as configuring interfaces, managing VLANs, and troubleshooting network issues, among others. It also can be used with other networking vendors like Juniper, Arista, etc.

