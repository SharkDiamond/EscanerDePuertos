import nmap
from tkinter import *
import requests


class Aplicacion():

	#CONSTRUCTOR
	def __init__(self):
		#CREANDO LA VENTANA
		self.__ventana =Tk()

		#CREANDO EL PANEL SUPERIOR
		self.__Frame=Frame()

		#CREANDO EL PANEL IZQUIERDO
		self.__Frame2=Frame()

		#CREANDO EL PANEL DERECHO
		self.__Frame3=Frame()

		#CREANDO EL PANEL INFERIOR
		self.__Frame4=Frame()

		#CREANDO EL FORMULARIO DE LA MAC ADDRESS
		self.__Mac=Entry(self.__Frame)

		#CREANDO EL LABEL DEL PANEL SUPERIOR DEL RESULTADO
		self.__Label=Label(self.__Frame)

		#CREANDO EL BOTON DE HACER LA PETICION DEL PANEL SUPERIOR
		self.__BotonMac=Button(self.__Frame)

		#CREANDO EL FORMULARIO DEL IP DEL PANEL INFERIOR
		self.__ipFormulario=Entry(self.__Frame4)

		#CREANDO EL BOTON DE ESCANEAR DEL PANEL INFERIOR
		self.__BotonEscaner=Button(self.__Frame4)

		#CREANDO EL TEXT AREAR DEL PANEL INFERIOR
		self.__textoMostrar=Text(self.__Frame4)

		#CREANDO EL FORMULARIOR DEL PUERTOS DEL PANEL INFERIOR
		self.__Puertos=Entry(self.__Frame4)

		#CREANDO LA BARRA DE TEXT AREA
		self.__barra=Scrollbar(self.__Frame4,command=self.__textoMostrar.yview)

		#CONSTRUYENDO LA VENTANA
		self.__ConstruyeVentana()


	def __ConstruyeVentana(self):

		#TITULO
		self.__ventana.title("Escaner De Puertos")

		#ICONO DE LA VENTANA
		self.__ventana.iconbitmap("Imagenes/reconocimiento.ico")

		#PARA QUE NO SE MODIFIQUE EL TAMAÑO DE LA VENTANA
		self.__ventana.resizable(False,False)

		#TAMAÑO DE LA VENTANA
		self.__ventana.geometry("700x400")

		#COLOR DE FONDO DE LA VENTANA
		self.__ventana.config(bg="#1D1C24")

		#CONSTRUYENDO INTERFAZ
		self.__ConstruyePanelDerecho()
		self.__ConstruyePanelIzquierdo()
		self.__ConstruyePanelSuperior()
		self.__ConstruyePanelInferior()

		self.__ventana.mainloop()


	def __hacerPeticion(self):

		#VALIDANDO DATOS INTRODUCIDOS EN EL FORMULARIO
		if self.__Mac.get().count(' ')==0 and len(self.__Mac.get())!=0 and len(self.__Mac.get())==17:

		#HACIENDO LA PETICION HACIA LA API DE MAC VENDORS
			Peticion=requests.get("https://api.macvendors.com/"+self.__Mac.get())

		#SI LA PETICION ES EXITOSA
			if Peticion.status_code==200:

			#ASIGNANDOLE EL VALOR DEVUELTO POR EL SERVIDOR AL LABEL
				self.__Label.config(text=Peticion.text,bg="#1D1C24",foreground="white")

		#SI NO ES EXITOSA LA PETICION
			else:

				self.__Label.config(text="La Peticion no pudo realizarse con exito",bg="#1D1C24",foreground="white")
	#SI LA VALIDACION DE LOS DATOS DEL FORMULARIO ES ERRONEA
		else:

			self.__Label.config(text="MAC ADDRESS MAL INTRODUCIDO",bg="#1D1C24",foreground="white")

	def __ConstruyePanelSuperior(self):

		#MARGEN CON LA VENTANA
		self.__Frame.pack(pady=10)

		#COLOR DE FONDO ANCHO Y ALTO
		self.__Frame.config(bg="#292935",width="400",height="150")

		#UBICACION DEL FORMULARIO DEL MAC ADDRESS
		self.__Mac.place(x=150,y=20)

		#COLOR DE FONDO Y DE LETRA
		self.__Mac.config(bg="#1D1C24",foreground="white")

		#UBICACION DEL RESULTADO
		self.__Label.place(x=150,y=90)

		#TEXTO COLOR DE FONDO Y DE LETRA DEL BOTON BUSCAR
		self.__BotonMac.config(text="Buscar",bg="#1D1C24",foreground="white", command=self.__hacerPeticion)

		#UBICACION DEL BOTON BUSCAR
		self.__BotonMac.place(x=150,y=50)

	def __ConstruyePanelInferior(self):

		self.__Frame4.pack(side="bottom",pady=10)
		self.__Frame4.config(bg="#292935",width="400",height="150")

		self.__ipFormulario.place(x=30,y=20)
		self.__ipFormulario.config(text="Mac-Address",bg="#1D1C24",foreground="white")
		self.__BotonEscaner.config(text="Empezar Escaneo",bg="#4D58DA",foreground="white")
		self.__BotonEscaner.place(x=30,y=100)

		self.__textoMostrar.place(x=165,y=9)
		self.__textoMostrar.config(bg="#1D1C24",width=28,height=8,foreground="white")
		self.__Puertos.config(bg="#1D1C24",foreground="white")
		self.__Puertos.place(x=30,y=60)
		self.__barra.place(x=375,y=9)


	def __ConstruyePanelIzquierdo(self):

		self.__Frame2.pack(side="left")
		self.__Frame2.config(bg="#292935",width="100",height="400")

	def __ConstruyePanelDerecho(self):

		self.__Frame3.pack(side="right")
		self.__Frame3.config(bg="#292935",width="100",height="400")



A=Aplicacion()

