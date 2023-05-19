from flask import request, abort
from netmiko import ConnectHandler
from netmiko.exceptions import SSHException


def test_fw_policy():
    params = request.json
    try:
        device = {
            'device_type': 'cisco_ios',
            'host': params['host'],
            'username': params['user'],
            'password': params['password'],
        }
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command('show ip int brief')
        return {'data': output}
    except SSHException as e:
        return str(e), 500
