import serial
import time 
import os
import csv
from datetime import datetime 

class Data:
    def __init__(self):
        self.data = {
            'time':'0',
            'Irms0':'0',
            'a':'0',
            'b':'0',
            'c':'0',
            'a-state':'0',
            'b-state':'0',
            'c-state':'0',
            'b0':'0',
            'b1':'0'
        }

    def collectData(self, line):
        line = line.split(':')
        key = line[0][1:]

        if key in self.data:
            self.data[key] = line[1]

        if key == "b1":
            self.writeToCsv()

    def writeToCsv(self):
        PATH = f"database/{datetime.now().strftime('%Y-%m-%d')}-log.csv"
        fileExists = os.path.isfile(PATH)
        with open(PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            if not fileExists:
                writer.writerow(self.data.keys())
            self.data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow(self.data.values())
            self.resetValues()


    def resetValues(self):
        for key in self.data.keys():
            self.data[key] = '0'


port = "/dev/ttyUSB0"
baudrate = 115200
data = Data()
serialPort = serial.Serial(port, baudrate, timeout=4)
time.sleep(2)

try:
    while True:
        if serialPort.in_waiting:
            line = serialPort.readline().decode("utf-8").rstrip()
            print(line)
            data.collectData(line)
finally:
    serialPort.close()