"""UDP messages reception class"""

import json
import socket

class UdpReceiver:
    """Class for UPD messages reception"""
    def __init__(self, conf: json):
        """UdpReceiver constructor"""
        self._ip = conf["ip"]
        self._port = conf["port"]
        self._buffer_size = conf["buffer_size"]
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self._ip, self._port))
        self._socket.settimeout(30)

    def listen(self) -> bytes:
        """Listen on configured socket"""
        try:
            data = self._socket.recv(self._buffer_size)
            return data
        except socket.error:
            print('socket.error - ' + socket.error)
            return None
