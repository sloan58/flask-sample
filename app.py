from flask import Flask, request
from netmiko import ConnectHandler
from netmiko.exceptions import SSHException

app = Flask(__name__)

@app.post("/palo/test-fw-policy")
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
        output = net_connect.send_command('show ip int brief', use_textfsm=True)
        return {'data': output}
    except SSHException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
