# Class DomoPy
from https://framagit.org/slallemand/Domoticzpy

This class aims to be an interface to Domoticz JSON API (domoticz.com).

## Install

```
pip install DomoPy
```

### Usage
```
domoticz_ip        = '192.168.0.1'
domoticz_port      = '8080'
domoticz_user      = 'user'
domoticz_pass      = 'password'

domoticz = DomoPy(domoticz_ip, domoticz_port, domoticz_user, domoticz_pass)

current_status = domoticz.getStatus()

print(current_status)
```
### License
This code uses the Apache License 2.0
