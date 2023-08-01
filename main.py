import json
import socket
import psutil
import platform
from datetime import datetime

import requests as requests
from MachineState import MachineState

data = {
    "machineState": []
}

data['machineState'].append(MachineState().__dict__)

data_json = json.dumps(data)
payload = {'json_payload': data_json}
r = requests.post("http://127.0.0.1:8000/api/v1/device", data=payload)





































