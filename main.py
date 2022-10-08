from configparser import ConfigParser
from miio import AirPurifierMiot
import typer
from typing import Tuple

app = typer.Typer()

@app.callback()
def callback():
    """
    Manage Xiaomi Mi Air Purifier CLI.
    """
    pass

@app.command('config')
def manage_config(
    set: Tuple[str, str] = typer.Option((None, None), help='Set device data <ip> <token>.')
):
    """Store your device data."""
    config = ConfigParser()
    ip, token = set
    if ip and token:
        config['device'] = {
            'ip': ip,
            'token': token
        }
        with open('config.ini', 'w') as f:
            config.write(f)
        print('Device config updated successfully.')
    else:
        config.read('config.ini')
        try:
            with open('config.ini', 'r') as f:
                config_data = config['device']
        except FileNotFoundError:
            print('Config not found. Use config --set to add device data.')
            return
        else:
            ip = config_data['ip']
            token = config_data['token']
            print(f'IP: {ip}')
            print(f'Token: {token}')


if __name__ == '__main__':
    app()
