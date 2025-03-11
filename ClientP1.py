import socket
import json
import numpy as np
import time
from datetime import datetime

def sensor_mock():
    return {
        "Temperature":round(np.random.uniform(10,35),2),
        "Humidity":round(np.random.uniform(20,90),2),
        "Irrigation":round(np.random.uniform(10,50),2),
        "RainGauge":round(np.random.uniform(0,50),2),
        "Timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
    except:
        print("No se pudo conectar al servidor")
    while True:
        sensor_data = sensor_mock()
        s.send(json.dumps(sensor_data).encode())
        time.sleep(3)

