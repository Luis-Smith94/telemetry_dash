"""
Bytes decoder modules
"""

from abc import ABC, abstractmethod
from struct import unpack

class IDecoder(ABC):
    """
    Decode packets thanks to given configuration
    """

    _conf: dict
    """
    Configuration of the decoder. Should contains decoded fields
    """

    @abstractmethod
    def __init__(self, conf: dict):
        """
        Abstract method for class initialisation
        """

    @abstractmethod
    def decode(self, raw_data: bytes) -> dict:
        """
        Abstract method for raw data decoing
        """

class ForzaDecoder(IDecoder):
    """
    Decode packets thanks to given configuration
    """

    def __init__(self, conf: dict):
        self._conf = conf

    def decode(self, raw_data: bytes) -> dict:
        """
        Decode given raw data
        """
        idx = 0
        res = {}
        for field in self._conf["fields"]:
            size = field["size"]
            signed = field["format"][0] == 'S'
            if field["format"] == "F32":
                res[field["name"]] = unpack('<f', raw_data[idx:idx+size])
            else:
                res[field["name"]] = int.from_bytes(raw_data[idx:idx+size],
                                                    byteorder="little",
                                                    signed=signed)
            idx += size

        return res
