## Overview
usage: `mip` `[--help]` `<command>` `[<args>]`

commands: `config`, `status`, `on`, `off`, `mode`, `level`, `favorite`, `day`, `night`, `led`

## List of commands

#### config
usage: `mip` `config` `[<options>]`

Manage device stored data.

commands: 

* `mip` `config` - read device stored data

options:
* `--set` - set device data <ip\> <token\>


#### status
usage: `mip` `status`

Get device status.

#### on
usage: `mip` `on`

Turn on a device.

#### off
usage: `mip` `off`

Turn off a device.

#### mode
usage: `mip` `mode` `[<mode>]`

Set device mode.

options: `Auto = 0` `Silent = 1` `Favorite = 2` `Fan = 3`


#### level
usage: `mip` `level` `[<level>]`

Set device fan speed level.

options: `1`, `2`, `3`

#### favorite
usage: `mip` `favorite` `[<rpm>]`

Set favorite motor speed (rpm).

options: RPM must be between 300 and 2300 and divisible by 10

#### day
usage: `mip` `day`

Set device to normal mode.

#### night
usage: `mip` `day`

Set device to night mode.

#### led
usage: `mip` `led` `[<level>]`

Set led brightness

options: `Bright = 0` `Dim = 1` `Off = 2`

