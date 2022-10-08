from miio import AirPurifierMiot
from config import load_config

def load_device():
    """Creates a device instance from config data."""
    config = load_config()
    if 'error' in config:
        return None
    else:
        try:
            device = AirPurifierMiot(ip=config['ip'], token=config['token'])
        except:
            return None
        return device
