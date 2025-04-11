import json
import time
import subprocess
from typing import Any
from pynng import Req0
from pynng.exceptions import ConnectionRefused

class NexDBClient:
    def __init__(self, address: str, daemon_path: str, max_attempts: int = 5):
        self._address = address
        self._daemon_path = daemon_path
        self._max_attempts = max_attempts
        self._socket = Req0()
        self._connected = False

    def connect(self) -> bool:
        attempt = 1
        daemon_started = False
        while attempt <= self._max_attempts:
            try:
                self._socket.dial(self._address, block=True)
                self._connected = True
                return True
            except ConnectionRefused:
                if not daemon_started:
                    print("⚙️ Starting daemon...")
                    self._start_daemon()
                    daemon_started = True
                time.sleep(2)
                attempt += 1
        print(f"❌ Could not connect to NexDB daemon after {self._max_attempts} attempts.")
        return False

    def _start_daemon(self):
        DETACHED_PROCESS = 0x00000008
        CREATE_NEW_PROCESS_GROUP = 0x00000200
        subprocess.Popen(
            ["python", self._daemon_path],
            creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
            close_fds=True
        )

    def _send_msg(self, command: str, params: dict):
        req_json = {"cmd": command, "params": params}
        self._socket.send(json.dumps(req_json).encode('utf-8'))

    def _receive_msg(self) -> tuple[str, Any]:
        resp_msg = self._socket.recv().decode('utf-8')
        msg_json = json.loads(resp_msg)
        return msg_json["type"], msg_json["data"]

    def start_engine_if_needed(self):
        if not self._connected:
            raise RuntimeError("Client is not connected. Call `connect()` first.")
        
        self._send_msg("ping", {})
        resp_type, resp_data = self._receive_msg()
        if resp_type != "pong":
            raise ValueError("NexDB daemon did not respond correctly to 'ping'.")
        server_status = resp_data["status"]
        if server_status == "operational":
            return
        
        print("⌚ Loading NexDB engine...")
        self._send_msg("start", {})
        resp_type, _ = self._receive_msg()
        if resp_type != "welcome":
            raise ValueError("NexDB engine did not start correctly.")
        
        print("👍 NexDB is operational.")

    def send_and_receive(self, command: str, params: dict) -> tuple[str, Any]:
        if not self._connected:
            raise RuntimeError("Client is not connected. Call `connect()` first.")
        self._send_msg(command, params)
        return self._receive_msg()

    def close(self):
        self._socket.close()
        self._connected = False
