import socket
import subprocess
import re
import sys
import time

def get_private_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def network_scan(ip):
    ip_parts = ip.split('.')
    subnet = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    devices = []
    cmd = 'arp -a'
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = result.communicate()[0].decode()

    lines = output.split('\n')
    for line in lines:
        match = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})', line)
        if match:
            device_ip = match.group(1)
            mac_address = match.group(0).split(' ')[1]
            if device_ip.startswith(subnet):
                try:
                    hostname = socket.gethostbyaddr(device_ip)[0]
                except socket.herror:
                    hostname = 'N/A'
                devices.append((hostname, device_ip, mac_address))

    return devices

private_ip = get_private_ip()
print("Your private IP address:", private_ip)

animation = "|/-\\"
idx = 0
loading = True

devices = network_scan(private_ip)

loading = False
print("\nDevices on your network:")
for device in devices:
    print("Name:", device[0])
    print("IP Address:", device[1])
    print("MAC Address:", device[2])
    print()
