import serial
import time

class arduino:
    def __init__(self,port,baudRate=9600):
        self.port = port
        self.baudRate = baudRate
        self.arduino = serial.Serial(self.port,self.baudRate)
    
    def enviarDatos(self,datos):
        self.arduino.write(datos.encode())

    def recibirDatos(self):
        return self.arduino.readline()
    
    def reinicarBuffer(self):
        self.arduino.reset_input_buffer()
