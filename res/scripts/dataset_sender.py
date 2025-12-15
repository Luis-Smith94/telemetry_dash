"""
Script for sending saved telemetrics
"""
import socket
import time

from typing import Generator
from sys import argv

DEFAULT_DATASET_FILEPATH = "../data/forza_dataset.txt"
DEFAULT_CONF_FILEPATH = "../conf/conf.json"

def read_line(path: str) -> bytes:
    """
    Lit la première ligne du fichier
    
    :param path: Fichier à lire
    :type path: str
    :return: Continue brut de la première ligne du fichier
    :rtype: bytes
    """
    # The binary data in little-endian format
    with open(path, "r") as file:
        hex_data = file.readline()
        # Combine the lines into a single hexadecimal string
        hex_data = "".join(hex_data).strip()
        # Convert the hexadecimal string to bytes and add it to the array
        return bytes.fromhex(hex_data)

def read_file(path: str) -> Generator[bytes]:
    """
    Lit le fichier fourni en utilisant un générateur
    
    :param path: Chemin vers le fichier à lire
    :type path: str
    :return: Générator de types pour chaque ligne du fichier
    :rtype: bytes
    """
    with open(path, 'r') as file:
        for line in file:
            data = bytes.fromhex("".join(line).strip())
            yield data

def send_dataset_to(path: str, ip: str, port: int):
    """
    Publie les données contenu dans le fichier, à destination de l'adresse fournie
    
    :param path: chemin vers le fichier contenant les données à envoyer
    :type path: str
    :param ip: Adresse IP où envoyer les données
    :type ip: str
    :param port: Port où envoyer les données
    :type port: int
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in read_file(path):
        s.sendto(data, (ip, port))
        time.sleep(1.0/60)

    s.close()

if __name__ == "__main__":
    dataset_path = DEFAULT_DATASET_FILEPATH
    conf_path = DEFAULT_CONF_FILEPATH

    if len(argv) > 1:
        for idx in range(1, len(argv)-1):
            if (argv[idx] == "-c" or argv[idx] == "--conf"):
                conf_path = argv[idx+1]
            elif (argv[idx] == "-d" or argv[idx] == "--dataset"):
                dataset_path = argv[idx+1]


    send_dataset_to(dataset_path, "127.0.0.1", 5300)
