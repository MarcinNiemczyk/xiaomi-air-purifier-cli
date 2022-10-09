import typer
from typing import Tuple
from miio import AirPurifierMiot
from miio.integrations.airpurifier.zhimi.airpurifier_miot import OperationMode
from config import load_config, save_config
from device import load_device

app = typer.Typer()
device = load_device()

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
    config = load_config()
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


@app.command('status')
def read_status():
    """Read device status."""
    if not device:
        print('Use config --set to add device.')
        return
    status = device.status()
    info = f"""
    Power: {status.power.upper()}
    PM2.5: {status.aqi}
    Temperature: {status.temperature} °C
    Humidity: {status.humidity}%
    Mode: {status.mode.name}
    Motor Speed: {status.motor_speed}
    Fan Level: {status.fan_level}
    Filter life: {status.filter_life_remaining}%
    """
    print(info)


@app.command('on')
def turn_on():
    """Turn on a device."""
    if not device:
        print('Use config --set to add device.')
        return
    device.on()
    print('Device is now ON.')


@app.command('off')
def turn_on():
    """Turn off a device."""
    if not device:
        print('Use config --set to add device.')
        return
    device.off()
    print('Device is now OFF.')


@app.command('mode')
def set_mode(mode: int = typer.Argument(None, help='Auto = 0 Silent = 1 Favorite = 2 Fan = 3')):
    """Set device mode."""
    if mode < 0 or mode > 3:
        print('Available modes: Auto = 0 Silent = 1 Favorite = 2 Fan = 3')
        return
    mode = OperationMode(mode)
    device.set_mode(mode)
    print(f'Device mode is now: {mode.name}.')


if __name__ == '__main__':
    app()
