import serial
import time 

port = "/dev/ttyUSB0"
baudrate = 115200

serialPort = serial.Serial(port, baudrate, timeout=4)
time.sleep(2)

try:
    while True:
        if serialPort.in_waiting:
            line = serialPort.readline().decode("utf-8").rstrip()
            print(line)
finally:
    serialPort.close()