from netmiko import ConnectHandler
from pprint import pprint

router = {"device_type": "cisco_ios",
       "host": "192.168.1.1",
       "user": "cisco",
       "pass": "cisco123"}

net_connect = ConnectHandler(ip=router["host"],
	          username=router["user"],
	          password=router["pass"],
	          device_type=router["device_type"])

interface_cli = net_connect.send_command("show run")

pprint(interface_cli)
