import typer
from typing import Tuple
from miio import AirPurifierMiot
from config import load_config, save_config

app = typer.Typer()
config = load_config()


@app.callback()
def callback():
    """
    Manage Xiaomi Mi Air Purifier CLI.
    """
    print('Running Xiaomi Mi Air Purifier command...')


@app.command('config')
def manage_config(
    set: Tuple[str, str] = typer.Option((None, None), help='Set device data <ip> <token>.')
):
    """Store your device data."""
    ip, token = set
    if ip and token:
        message = save_config(ip, token)
        print(message)
    else:
        if 'error' in config:
            print(config['error'])
        else:
            print(f"IP: {config['ip']}")
            print(f"Token: {config['token']}")


if __name__ == '__main__':
    app()
