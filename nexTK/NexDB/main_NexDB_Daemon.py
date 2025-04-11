import os
import pynng
from message_queue_helpers import send_msg, receive_msg

def load_controller(database_url:str, data_store_path:str):
    from time import time
    start_t = time()
    from CommandController import CommandController
    load_duration = time() - start_t
    return CommandController(database_url, data_store_path, True), load_duration


def main(database_url:str, message_queue_ipc_socket:str, data_store_path:str):
    controller = None
    with pynng.Rep0(listen=message_queue_ipc_socket) as rep_socket:
        print("message queue listener started")

        while True:

            success, command, params = receive_msg(rep_socket)
            if not success:
                continue

            if command == "ping":
                send_msg(rep_socket, "pong", {"status": "waiting" if controller is None else "operational"})
                continue
            elif command == "start":
                if controller is None:
                    controller, load_time = load_controller(database_url, data_store_path)
                send_msg(rep_socket, "welcome", {"loading_time":load_time})
                continue
            elif command == "shutdown":
                send_msg(rep_socket, "bye_bye", {})
                rep_socket.close()
                break

            if controller is None:
                send_msg(rep_socket, "request_error", "You cannot send engine specific commands yet. Use the 'start' command to load the engine.")
                continue
            resp_type, resp_data = controller.execute(command, params)
            send_msg(rep_socket, resp_type, resp_data)


if __name__ == '__main__':
    data_path = "./../NexDB_DATA"
    if not os.path.exists(data_path):
        os.makedirs(data_path, exist_ok=True)
    store_path = f"{data_path}/datasets"
    db_url = f"sqlite:///{data_path}/NexDB.db"
    mq_socket = "ipc:///tmp/oscar_nexus_nexdb_daemon"
    main(db_url, mq_socket, store_path)