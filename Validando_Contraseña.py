import re 
from tkinter import * 

def Contraseña():
    cadena=entrada.get()
    patron="^(?=.*[A-Z])(?=(?:\D*\d){3}\D*$)(?=.*[a-z]{3})(?=.*[$@$!%*?&(]{3}).{6,10}$"
    if(re.match(patron,cadena)):
        lblResultado=Label(ventana,text="Contraseña Valida: "+ entrada.get(),
                      font=("Agency FB",19)).place(x=40,y=50)
    
    else:
        lblResultado=Label(ventana,text="Contraseña No valida: "+ entrada.get(),
                      font=("Agency FB",19)).place(x=40,y=50)

def BorrarTexto():
        lblResultado=Label(ventana,text="                                                                          ",
                       font=("Agency FB",19)).place(x=40,y=50)

ventana = Tk() 
ventana.geometry("500x270+100+100") 
ventana.title("Validar Una contraseña") 

lblUsuario=Label(text="Ingrese la cadena: ",font=("Agency FB",16)).place(x=20,y=10)


entrada = StringVar()

textUsuario = Entry(ventana,textvariable=entrada,width=42).place(x=150,y=20)

btnContraseña=Button(ventana,text="Validar_Contraseña",command=Contraseña,font=("Agency FB",14),
                  width=20).place(x=10,y=90)

btnLimpiar=Button(ventana,text="Limpiar",command=BorrarTexto,font=("Agency FB",14),width=8).place(x=420,y=15)
