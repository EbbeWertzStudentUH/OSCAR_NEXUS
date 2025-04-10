
from CommandController import CommandController
import json
from typing import Any
import pynng


def _send_msg(socket:pynng.Rep0, resp_type:str, data:Any):
    resp_json = {"type": resp_type, "data": data}
    print(f"sent: {resp_type} - {data}")
    socket.send(json.dumps(resp_json).encode('utf-8'))

def _receive_msg(socket:pynng.Rep0) -> tuple[bool, str, dict]:
    request_msg = socket.recv().decode('utf-8')
    try:
        msg_json = json.loads(request_msg)

        if "cmd" not in msg_json or "params" not in msg_json:
            _send_msg(socket, "request_error", "Request should be json encoded with a 'cmd' and 'params' field.")
            return False, '', {}

        command, params = msg_json["cmd"], msg_json["params"]
        print(f"got: {command} - {params}")
        return True, command, params

    except TypeError:
        _send_msg(socket, "request_error", "Request params should be valid json syntax")
        return False, '', {}


def main(database_url:str, message_queue_ipc_socket:str):
    controller = CommandController(database_url)

    with pynng.Rep0(listen=message_queue_ipc_socket) as rep_socket:
        print("server started")

        while True:

            success, command, params = _receive_msg(rep_socket)
            if not success:
                continue

            if command == "shutdown":
                rep_socket.close()
                break

            resp_type, resp_data = controller.execute(command, params)
            _send_msg(rep_socket, resp_type, resp_data)


if __name__ == '__main__':
    db_url = "sqlite:///NexDB.db"
    mq_socket = "ipc:///tmp/oscar_nexus_nexdb_daemon"
    main(db_url, mq_socket)