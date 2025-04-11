import json
from typing import Any
from pynng import Rep0


def send_msg(socket:Rep0, resp_type:str, data:Any):
    resp_json = {"type": resp_type, "data": data}
    print(f"sent: {resp_type} - {data}")
    socket.send(json.dumps(resp_json).encode('utf-8'))

def receive_msg(socket:Rep0) -> tuple[bool, str, dict]:
    request_msg = socket.recv().decode('utf-8')
    try:
        msg_json = json.loads(request_msg)

        if "cmd" not in msg_json or "params" not in msg_json:
            send_msg(socket, "request_error", "Request should be json encoded with a 'cmd' and 'params' field.")
            return False, '', {}

        command, params = msg_json["cmd"], msg_json["params"]
        print(f"got: {command} - {params}")
        return True, command, params

    except TypeError:
        send_msg(socket, "request_error", "Request params should be valid json syntax")
        return False, '', {}