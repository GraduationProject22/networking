import json
from utils.get_ip_address import get_ip_address


def add_ip_address(file_name):
    ip = get_ip_address()
    with open(file_name, 'r') as f:
        data = json.load(f)

    data['ip'] = ip

    with open(file_name, 'w') as f:
        json.dump(data, f)
