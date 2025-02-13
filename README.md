# pygui_rpc
rpc server and client for pyautogui, you can make pyautogui calls with rpc

## Quick start:

Server side:

```
## bash code
DISPLAY=:0 python server.py
```

Client side:

```
## python code
from client import Client

client = Client('http://localhost:8006')
ret = client.run('moveTo', 10, 20)
```

You can make any pyautogui method by `client.run(<method_name>, *<method_args>, **<method_kwargs>)`
