from nmap.nmap import PortScanner
from tkinter import *



class Aplicacion(PortScanner):


	def __init__(self):

		self.__ventana =Tk()
		self.__Frame=Frame()
		self.__Frame2=Frame()
		self.__Frame3=Frame()
		self.__Frame4=Frame()
		self.__Mac=Entry(self.__Frame)
		self.__Label=Label(self.__Frame)
		self.__ipFormulario=Entry(self.__Frame4)
		self.__BotonEscaner=Button(self.__Frame4)
		self.__textoMostrar=Text(self.__Frame4)

		self.__barra=Scrollbar(self.__Frame4,command=self.__textoMostrar.yview)

		self.__ConstruyeVentana()


	def __ConstruyeVentana(self):

		#Titulo
		self.__ventana.title("Escaner De Puertos")
		self.__ventana.iconbitmap("Imagenes/reconocimiento.ico")
		self.__ventana.resizable(False,False)
		self.__ventana.geometry("700x400")
		self.__ventana.config(bg="#1D1C24")

		self.__ConstruyePanelDerecho()
		self.__ConstruyePanelIzquierdo()
		self.__ConstruyePanelSuperior()
		self.__ConstruyePanelInferior()

		self.__ventana.mainloop()


	def __ConstruyePanelSuperior(self):

		self.__Frame.pack(pady=10)
		self.__Frame.config(bg="#292935",width="400",height="150")


		self.__Mac.place(x=150,y=20)
		self.__Mac.config(text="Mac-Address",bg="#1D1C24",foreground="white")
		self.__Label.place(x=150,y=60)
		self.__Label.config(text="Mac-Address")


	def __ConstruyePanelInferior(self):

		self.__Frame4.pack(side="bottom",pady=10)
		self.__Frame4.config(bg="#292935",width="400",height="150")

		self.__ipFormulario.place(x=30,y=40)
		self.__ipFormulario.config(text="Mac-Address",bg="#1D1C24",foreground="white")
		self.__BotonEscaner.config(text="Empezar Escaneo",bg="#4D58DA",foreground="white")
		self.__BotonEscaner.place(x=30,y=80)

		self.__textoMostrar.place(x=165,y=9)
		self.__textoMostrar.config(bg="#1D1C24",width=28,height=8,foreground="white")

		self.__barra.place(x=375,y=9)


	def __ConstruyePanelIzquierdo(self):

		self.__Frame2.pack(side="left")
		self.__Frame2.config(bg="#292935",width="100",height="400")



	def __ConstruyePanelDerecho(self):

		self.__Frame3.pack(side="right")
		self.__Frame3.config(bg="#292935",width="100",height="400")




apli=Aplicacion()
