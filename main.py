from tkinter import *
import time
import numpy as np 
from threading import Thread
import cv2
from PIL import Image
from PIL import ImageTk


camera = cv2.VideoCapture(0)
panel = None
root = None
path = './Imagenes/{}'
encenderCamara = None
apagarCamara = None
Icamara = None
fondo = '#203500'
letraRojo = 'red'
letraBlanca = 'white'
from PCA9685 import PCA9685

motorPos1 = 100
motorPos0 = 50

def moverMotor(motor,angulo):
    global motorPos0,motorPos1
    pwm = PCA9685()
    pwm.setPWMFreq(50)
    if motor:
        if angulo:
            motorPos1 = motorPos1 + 5
            if motorPos1 > 180: 
                motorPos1 = 180
            pwm.setRotationAngle(1,motorPos1)
        else:
            motorPos1 = motorPos1 - 5
            if motorPos1 < 0 :
                motorPos1 = 0
            pwm.setRotationAngle(0,motorPos1)
    else:
        if angulo:
            motorPos0 = motorPos0 + 5
            if motorPos0 > 180: 
                motorPos0 = 180
            pwm.setRotationAngle(0,motorPos0)
        else:
            motorPos0 = motorPos0 - 5
            if motorPos0 < 0 :
                motorPos0 = 0
            pwm.setRotationAngle(0,motorPos0)
    print(motorPos1)
    print(motrPos2)
    pwm.exit_PCA9685()

def Camara():
    _,frame = camera.read()
    frame = cv2.resize(frame,(512,512))
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)
    panel.configure(image=frame)
    panel.image = frame
    if encenderCamara['state'] == DISABLED:
        panel.after(1,Camara)
    else:
        panel.configure(image=Icamara)
        panel.image = Icamara
        
def ApagarCamara():
    encenderCamara.configure(state=NORMAL)
    apagarCamara.configure(state=DISABLED)

def EncenderCamara():
    apagarCamara.configure(state=NORMAL)
    encenderCamara.configure(state=DISABLED)
    Camara()

def ponerTitulo(label):
    label.configure(fg='#419f00',font=('MS Sans Serif',25,'bold'))

def ponerSubTitulo(label):
    label.configure(fg='white',font=('MS Sans Serif',15))

    
if  __name__ == '__main__':
    root = Tk()
    root.resizable(0,0)
    #root.iconbitmap(path.format('chile-habanero.ico'))
    root.title('Proyecto Chile Habanero')
    root.configure(bg=fondo)

    print(xx)

    header = Frame(root,bg=fondo)
    body = Frame(root,bg=fondo)
    leftBody = Frame(body,bg=fondo)
    leftBodyTop = Frame(leftBody,bg=fondo)
    leftBodyBot = Frame(leftBody,bg=fondo)
    rightBody = Frame(body,bg=fondo)
    footer = Frame(root,bg=fondo)
    
    header.grid(row=0,column=0)
    body.grid(row=1,column=0)
    leftBody.grid(row=0,column=0)
    leftBodyTop.grid(row=0,column=0)
    leftBodyBot.grid(row=1,column=0)
    rightBody.grid(row=0,column=1)
    footer.grid(row=2,column=0)

    #Header
    Icicata = PhotoImage(file=path.format('cicata.png'))
    logoCicata = Label(header,image=Icicata,bg=fondo)
    labelTitulo = Label(header,text="INVERNADERO:  CHILE HABANERO",bg=fondo)
    ponerTitulo(labelTitulo)
    Ipolitecnico = PhotoImage(file=path.format('politecnico.png'))
    logoPolitecnico = Label(header,image=Ipolitecnico,bg=fondo)

    logoCicata.grid(row=0,column=0,padx=5)
    labelTitulo.grid(row=0,column=1,padx=0)
    logoPolitecnico.grid(row=0,column=2)
    
    
    #Body
    #lefBody
    encenderCamara = Button(leftBodyTop,text='Activar',command=EncenderCamara,width=10)
    apagarCamara = Button(leftBodyTop,text='Desactivar',command=ApagarCamara,width=10)
    encenderCamara.configure(bg=fondo)
    apagarCamara.configure(bg=fondo)
    ponerSubTitulo(encenderCamara)
    ponerSubTitulo(apagarCamara)
    
    encenderCamara.grid(row=0,column=0,padx=5,pady=5)
    apagarCamara.grid(row=0,column=1,padx=5,pady=5)
    
    IflechaArr = PhotoImage(file=path.format('flechaArr.png'))
    IflechaAba = PhotoImage(file=path.format('flechaAba.png'))
    IflechaDer = PhotoImage(file=path.format('flechaDer.png'))
    IflechaIzq = PhotoImage(file=path.format('flechaIzq.png'))
    Arriba = Button(leftBodyBot,image=IflechaArr,bg=fondo)
    Abajo = Button(leftBodyBot,image=IflechaAba,bg=fondo) 
    Izq = Button(leftBodyBot,image=IflechaIzq,bg=fondo)
    Der = Button(leftBodyBot,image=IflechaDer,bg=fondo)

    Arriba.configure(command=lambda: moverMotor(False,True))
    Abajo.configure(command=lambda: moverMotor(False,False))
    Izq.configure(command=lambda: moverMotor(True,False))
    Der.configure(command=lambda: moverMotor(True,True))
    
    Arriba.grid(row=0,column=1,padx=5,pady=5)
    Izq.grid(row=1,column=0,padx=5,pady=5)
    Abajo.grid(row=1,column=1,padx=5,pady=5)
    Der.grid(row=1,column=2,padx=5,pady=5)
    
    #rightBody
    Icamara = PhotoImage(file=path.format('camera.png'))
    panel = Label(rightBody,image=Icamara,width=500,height=500)
    panel.grid(row=0,column=0)
    
    
    #footer
    Arduino = Button(footer,text='Conectar',bg=fondo,width=20)
    Puerto = Entry(footer,font=('Helvetica', 15, 'bold'),width=20)
    Luz = Button(footer,text='LUZ',bg=fondo,width=20)
    GuadrarDatos = Button(footer,text='Guadar Datos',bg=fondo,width=20)
    Humedad = Label(footer,text='Humedad: 0.0 %',bg=fondo,width=20,anchor='w')
    Temperatura = Label(footer,text='Temperatura: 0.0 °C',bg=fondo,width=20,anchor='w')

    Puerto.insert(END,'/dev/ttyUSB0')
    ponerSubTitulo(Humedad)
    ponerSubTitulo(Arduino)
    ponerSubTitulo(Luz)
    ponerSubTitulo(GuadrarDatos)
    ponerSubTitulo(Temperatura)
    
    Arduino.grid(row=0,column=0,padx=5,pady=5)
    Puerto.grid(row=0,column=1,padx=5,pady=5)
    Luz.grid(row=1,column=0,padx=5,pady=5)
    GuadrarDatos.grid(row=1,column=1,padx=5,pady=5)
    Humedad.grid(row=0,column=2,padx=5,pady=5)
    Temperatura.grid(row=1,column=2,padx=5,pady=5)


    root.mainloop()
    camera.release()
