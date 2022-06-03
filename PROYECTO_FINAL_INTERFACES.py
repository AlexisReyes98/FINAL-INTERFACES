import cv2
import tkinter as tk
import pyttsx3
import threading
import winsound
from tkinter import *
import tkinter.font as TkFont
from PIL import Image, ImageTk

""" Creamos la ventana principal con sus características """    
root=Tk() 
root.geometry("700x600+0+0")#tamaño de la ventana principal
root.title(' ***********              Sistema MUVI - Detector de movimiento        ***********')#titulo de la ventana 
root.config(bg="white")#color de fondo
fondo = PhotoImage(file="muvi5.gif")#definir la imagen de fondo 
lblFondo=Label(root,image=fondo).place(x=0,y=10)#posición de la imagen principal de fondo

""" Antes de usar nuestra cámara web, configuraremos el primer fotograma / fotograma inicial en 'None'."""
status_list=[None,None]

#función para activar la alarma
def sonido():
    freq=2000 #frecuencia del sonido
    duration=4000 # 4 segundos de duración
    a=winsound.Beep(freq,duration)#el sonido dura 4 segundos con una frecuencia alta.
    
#Función para que al inicio de la ejecución de la interfaz se escuche un mensaje de presentación     
def presentacion():

    winsound.PlaySound("presen", winsound.SND_FILENAME)
    
#Función para escuchar las recomendaciones para el uso del detector de movimiento
def Recomendacion():

    winsound.PlaySound("recomendaciones", winsound.SND_FILENAME)
    
# Función para ver las recomendaciones en una subventana
def LeerReco():
    
    win3=Toplevel()
    win3.geometry('700x550+700+100')
    win3.title('Recomendaciones')
    win3.config(bg='white')
    #fondo para ventana
    img_3 = Image.open("leerreco.gif")      
    img3_fondo = ImageTk.PhotoImage(img_3)

    label7 = tk.Label (win3,image = img3_fondo) 
    label7.image = img3_fondo

    # Posición de la imagen 
    label7.place (x = 0 , y = 0,relwidth=1, relheight=1 ) 

    sub_btnnew=tk.Button(win3,text = "Cerrar",command =win3.destroy,font=("Tahoma",16),fg='black',bg="red")
    sub_btnnew.place(x=250,y=500)
    
#Función para que se detecte un movimiento en tiempo real y se produzca el sonido de alarma.
def activar_detector():
    
    #al iniciar la ejecución del detector de movimiento se escucha un mensaje que dice "el detector a sido activado."
    winsound.PlaySound("detector", winsound.SND_FILENAME)
    """ Hemos establecido un valor 'None' para nuestro marco inicial. Luego, el video se captura desde la cámara web con la ayuda
        del comando "cv2.VideoCapture". Ahora, estamos leyendo los fotogramas del video capturado en un bucle while. """
    video=cv2.VideoCapture(0)
    initial_frame = None
    while True:
        check, frame = video.read()
        frame = cv2.flip(frame,1)
        status=0
        #Aquí, hemos convertido nuestro marco en color gris y lo hemos hecho un poco borroso.
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray_frame=cv2.GaussianBlur(gray_frame,(25,25),0)
        blur_frame = cv2.blur(gray_frame, (5,5))
        
        if initial_frame is None:
            initial_frame = blur_frame
            continue
        """ Dado que mantuvimos nuestro fotograma inicial en "None" y si sigue siendo el mismo, estamos reenviando el blur_frame a
            nuestro initial_frame. Entonces, el blur_frame será nuestro marco inicial. """
        delta_frame=cv2.absdiff(initial_frame,blur_frame)
        threshold_frame=cv2.threshold(delta_frame,35,255, cv2.THRESH_BINARY)[1]

        """ Aquí, estamos encontrando la diferencia entre nuestro initial_frame y blur_frame y luego lo convertimos en una imagen binaria usando
            un método llamado Image Thresholding. En este método, especificamos un cierto valor en la función y si el valor de píxel de la imagen
            es mayor que el valor especificado, a ese píxel se le asigna el valor del color blanco (200). Si el valor de píxel es menor que el valor
            especificado, a ese píxel se le asigna el valor de color negro (0). De esta forma obtendremos una imagen binaria de dos colores, blanco y negro.
            Esta imagen binaria ahora se usa para encontrar el contorno alrededor del objeto detectado.  """
        
        (contours,_)=cv2.findContours(threshold_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            status=status + 1
            (x, y, w, h)=cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)
        status_list.append(status)
        """ Ahora, estamos encontrando los contornos usando el umbral_frame. Hemos especificado que, si el área del contorno es mayor que 5000,
            se dibuja un cuadro rectangular alrededor del objeto. Luego, estamos actualizando nuestro status_list agregando el valor del estado en él. 
            ------------------------------------------------------------------------------------------------------------------------------------------
            Este bloque de código se utiliza para hacer sonar una alarma si se detecta un objeto en movimiento. Aquí, si el último valor de status_list
            es mayor o igual a '1' y el último valor de segundo es '0', entonces se inicia una alarma usando la función threading.Thread ().  """  
        if status_list[-1]>= 1 and status_list[-2]==0:
            alarm = threading.Thread(target=sonido)#llamado a el método sonido
            alarm.start()

        """ Luego usamos cv2.imshow para mostrar nuestra ventana de marco y especificamos una clave para cerrarla
            en nuestro caso al presionar la tecla q """
       
        cv2.imshow('Detector de movimiento activo', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            quit()
            break
    alarm_sound.stop()
    video.release()
    cv2.destroyAllWindows()

""" función para cerrar la ventana principal de la interfaz al presionar el botón salir """
def close_window():

    root.destroy()
    
""" función para crear una nueva ventana al presionar el boton de ayuda, en esta función se definen diversos características para la ventana """
def nuevaventana():

    win=Toplevel()#especificar que sera una subventana de la principal
    win.geometry('580x400+700+100')#tamaño de la ventana
    win.title('Ayuda')#titulo de la ventana
    win.config(bg='white')#color de fondo de la ventana
    #etiqueta para un titulo dentro de la ventana
    name_label4 = tk.Label(win, text = 'Recomendaciones más importantes', font=("Tahoma", 20), bg="gold",fg="black")
    name_label4.place(x=130,y=0)#posición de la etiqueta dentro de la ventana
    #fondo para la subventana
    img_2 = Image.open("MUVI.gif")      
    img2_fondo = ImageTk.PhotoImage(img_2)
    #se coloca el fondo.
    label1 = tk.Label (win,image = img2_fondo) 
    label1.image = img2_fondo
    # Posición de la imagen
    label1.place (x = 0 , y = 0,relwidth=1, relheight=1 )
    """definir los botones y sus características"""
    #este botón sirve para que al presionarlo llame a la función Recomendación y 
    sub_btn4=tk.Button(win,text = "Escuchar recomendaciones",command =Recomendacion ,font=("Tahoma",16),fg='black',bg="aquamarine")
    sub_btn4.place(x=150,y=60)

    sub_btn5=tk.Button(win,text = "Ver recomendaciones",command =LeerReco,font=("Tahoma",16),fg='black',bg="green yellow")
    sub_btn5.place(x=150,y=130)

    
    sub_btn6=tk.Button(win,text = "Cerrar",command =win.destroy,font=("Tahoma",16),fg='black',bg="red")
    sub_btn6.place(x=150,y=200)

#MAIN PRINCIPAL
name_label = tk.Label(root, text = '  ***   ¿Desea activar el detector?   ***    ', font=("Tahoma", 14), bg="lavender",fg="black",width="60")
name_label.place(x=50,y=0)
#llamado a la función para emitir una pequeña presentación con el usuario
presentacion()

# Botón que llamará a la función de lectura  
sub_btn=tk.Button(root,text = "Activar",command =activar_detector ,font=("Tahoma",18),fg='black',bg="lawn green")
sub_btn.place(x=400,y=60)
#boton que llama a la función para cerrar la ventana principal
sub_btn2=tk.Button(root,text = "Salir",command = close_window,font=("Tahoma",18),fg='black',bg="red")
sub_btn2.place(x=400,y=125)
#boton que llama a la función de ayuda
sub_btn3=tk.Button(root,text = "Ayuda",command =nuevaventana,font=("Tahoma",18),fg='black',bg="dark violet")
sub_btn3.place(x=400,y=190)





