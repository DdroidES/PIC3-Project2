import socket
import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

URL = "postgresql://basededatospic3_user:m9C8QTkGbXqFebUy9LRpEvHLUvHHwRX4@dpg-cv3kbg3qf0us73fcm05g-a.frankfurt-postgres.render.com/basededatospic3"
engine = create_engine(URL,echo=True,future=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Humidity(Base):
    __tablename__ = "humidity"
    timestamp = Column(String(255), primary_key=True, nullable=False)
    value = Column(Float)

class Irrigation(Base):
    __tablename__ = "irrigation"
    timestamp = Column(String(255), ForeignKey("humidity.timestamp"),primary_key=True, nullable=False)
    value = Column(Float)

class RainGauge(Base):
    __tablename__ = "raingauge"
    timestamp = Column(String(255), ForeignKey("humidity.timestamp"),primary_key=True, nullable=False)
    value = Column(Float)

class Temperature(Base):
    __tablename__ = "temperature"
    timestamp = Column(String(255), ForeignKey("humidity.timestamp"),primary_key=True, nullable=False)
    value = Column(Float)


def save_data(sensordata):
    date = sensordata['Timestamp']
    session.add_all([
        Humidity(timestamp=date, value=sensordata['Humidity']),
        Irrigation(timestamp=date, value=sensordata['Irrigation']),
        RainGauge(timestamp=date, value=sensordata['RainGauge']),
        Temperature(timestamp=date, value=sensordata['Temperature']),
    ])
    session.commit()

HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        elif data:
            sensor_data = json.loads(data)
            save_data(sensor_data)


