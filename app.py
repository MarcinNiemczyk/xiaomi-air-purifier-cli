import typer
from typing import Tuple
from miio import AirPurifierMiot
from miio.integrations.airpurifier.zhimi.airpurifier_miot import OperationMode, LedBrightness
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
    Favorite speed: {status.favorite_rpm}rpm
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
    if mode is None:
        print('Available modes: Auto = 0 Silent = 1 Favorite = 2 Fan = 3')
        return
    if mode < 0 or mode > 3:
        print('Available modes: Auto = 0 Silent = 1 Favorite = 2 Fan = 3')
        return
    mode = OperationMode(mode)
    device.set_mode(mode)
    print(f'Device mode is now: {mode.name}.')


@app.command('level')
def set_level(level: int = typer.Argument(None, help='Set device fan level speed (1-3).')):
    """Set device fan level speed."""
    if level is None:
        print('Available fan speed levels: 1-3')
        return
    if level < 1 or level > 3:
        print('Available fan speed levels: 1-3')
        return
    device.set_fan_level(level)
    print(f'Device fan speed level is now: {level}.')


@app.command('favorite')
def set_favorite(rpm: int = typer.Argument(None, help='RPM must be between 300 and 2200 and divisible by 10')):
    """Set favorite motor speed (rpm)."""
    if rpm is None:
        print('RPM must be between 300 and 2200 and divisible by 10')
        return
    if rpm < 300 or rpm > 2200 or rpm % 10 != 0:
        print('RPM must be between 300 and 2200 and divisible by 10')
        return
    device.set_favorite_rpm(rpm)
    print(f'Device favorite rpm is now: {rpm}.')


@app.command('day')
def set_day_mode():
    """Set device to day mode."""
    device.set_mode(OperationMode(0))
    device.set_led_brightness(LedBrightness(0))
    print('Day mode is now active.')


@app.command('night')
def set_night_mode():
    """Set device to night mode."""
    device.set_mode(OperationMode(1))
    device.set_led_brightness(LedBrightness(2))
    print('Night mode is now active.')


if __name__ == '__main__':
    app()
