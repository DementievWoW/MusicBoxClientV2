import json
import websockets
import asyncio
import uuid

from fileHandler import readRuntimeLogs, readStartLogs

password = 'qwer'
UUID = str(uuid.UUID(int=uuid.getnode()))
url = "ws://localhost:8000/ws/?password=" + password + "&UUID=" + UUID
from MachineState import MachineState

pathStartLogs = 'C:\\Users\\Demen\\PycharmProjects\\MusicBoxClientV2.\\TestLogs\\bubuka_launcher.log'
pathRuntimeLogs = 'C:\\Users\\Demen\\PycharmProjects\\MusicBoxClientV2\\TestLogs\\bubuka.log'


def getMachineStateJson():
    data = {
        "UUID": str(uuid.UUID(int=uuid.getnode())),
        "machineState": [],
        "password": "qwer",
        "StartLogs": [],
        "RuntimeLogs": [],
    }
    data['StartLogs'].append(readStartLogs(pathStartLogs))
    data['RuntimeLogs'].append(readRuntimeLogs(pathRuntimeLogs))
    data['machineState'].append(MachineState().__dict__)

    data_json = json.dumps(data, ensure_ascii=False)
    return data_json

async def listen(url):
    async with websockets.connect(url) as websocket:
        while 1:
            msg = await websocket.recv()
            print(msg)
            await websocket.send(getMachineStateJson())




asyncio.get_event_loop().run_until_complete(listen(url))






























