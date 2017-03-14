from jnpr.junos import Device
from getpass import getpass
import sys
import json
import yaml

hostname = raw_input("Enter Host Name:")
username = raw_input("Device user Name:")
password = raw_input("Device Password:")

# NETCONF session over SSH
dev = Device(host=hostname,user=username,passwd=password)
# Telnet connection
#dev = Device(host=hostname, user=username, passwd=password, mode='telnet',port='23', gather_facts=True)

# Serial console connection
#dev = Device(host=hostname, user=username, passwd=password, mode='serial',port='/dev/ttyUSB0', gather_facts=True)

try:
    dev.open()
except ConnectError as err:
    print ("Cannot connect to device: {0}".format(err))
except Exception as err:
    print (err)
    sys.exit(1)

print (dev.facts)
print(yaml.dump(dev.facts))
print(json.dumps(dev.facts))
dev.close()


