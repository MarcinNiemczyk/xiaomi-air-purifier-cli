from configparser import ConfigParser

config = ConfigParser()

def load_config() -> dict:
    """Reads device config and returns ip, token key-value pair."""
    config.read('config.ini')
    try:
        with open('config.ini', 'r') as f:
            config_data = config['device']
    except FileNotFoundError:
        return {'error': 'Config not found. Use config --set to add device data.'}
    else:
        ip = config_data['ip']
        token = config_data['token']
        return {'ip': ip, 'token': token}


def save_config(ip: str, token: str):
    """Store or update device data config."""
    config['device'] = {
            'ip': ip,
            'token': token
        }
    with open('config.ini', 'w') as f:
        config.write(f)
    return 'Device config updated successfully.'
