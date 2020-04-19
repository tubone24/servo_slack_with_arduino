from time import sleep
import serial
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class WipeData(BaseModel):
    delay: int
    time: int
    port: Optional[str] = "COM3"
    baudrate: Optional[int] = 9200


class MoveData(BaseModel):
    angle: int
    port: Optional[str] = "COM3"
    baudrate: Optional[int] = 9200


@app.get('/')
async def hello():
    return {"text": "Hello Arduino"}


@app.post('/wipe')
async def wipe(data: WipeData):
    wipe_servo(data.delay, data.time, data.port, data.baudrate)
    return {"return": f"request ok: {data.delay}, {data.time}, {data.port}, {data.baudrate}"}


@app.post('/move')
async def move(data: MoveData):
    move_servo_angle(data.angle, data.port, data.baudrate)
    return {"return": f"request ok: {data.angle}, {data.port}, {data.baudrate}"}


def move_servo_angle(angle, port, baudrate):
    my_serial = serial.Serial()
    my_serial.port = port
    my_serial.baudrate = baudrate
    my_serial.setDTR(False)
    my_serial.open()
    my_serial.write(str(angle).encode())
    my_serial.close()


def wipe_servo(delay, time, port, baudrate):
    my_serial = serial.Serial()
    my_serial.port = port
    my_serial.baudrate = baudrate
    for _ in range(time):
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"20")
        my_serial.close()
        sleep(int(delay))
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"90")
        my_serial.close()
        sleep(delay)
        my_serial.setDTR(False)
        my_serial.open()
        my_serial.write(b"160")
        my_serial.close()
        sleep(delay)
