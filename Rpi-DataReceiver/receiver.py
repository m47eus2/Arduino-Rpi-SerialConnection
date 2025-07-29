import serial
import time 
import os
import csv
import glob
import pandas as pd
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
            'b1':'0',
            'p':'0',
            'e':'0'
        }

        self.energy = self.getLastEnergyValue()
        self.powerKeys = ['Irms0','a','b','c']
        self.stateKeys = ['a-state','b-state','c-state','b0','b1']

    def collectData(self, line):
        line = line.split(':')
        key = line[0][1:]

        if key in self.powerKeys:
            self.data[key] = self.currentToPower(line[1])
        if key in self.stateKeys:
            self.data[key] = line[1]
        if key == 'b1':
            self.writeToCsv()

    def writeToCsv(self):
        PATH = f"database/{datetime.now().strftime('%Y-%m-%d')}-log.csv"
        fileExists = os.path.isfile(PATH)
        with open(PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            if not fileExists:
                writer.writerow(self.data.keys())
            self.fillRow()
            writer.writerow(self.data.values())
            self.resetValues()

    def fillRow(self):
        self.data['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.energy += float(self.data['p'])
        self.data['e'] = self.energy

    def currentToPower(self, current):
        return (float(current)*230.0)/1000.0
    
    def getLastEnergyValue(self):
        files = glob.glob("database/*-log.csv")
        if files:
            PATH = sorted(files)[-1]
            csvFile=pd.read_csv(PATH)
            csvFile=csvFile.tail(1)
            return float(csvFile['e'].values[0])
        else:
            return 0.0


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
        else:
            time.sleep(0.01)
finally:
    serialPort.close()