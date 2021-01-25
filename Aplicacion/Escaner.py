from nmap.nmap import PortScanner
from tkinter import *


class Aplicacion(PortScanner):
	

	def __init__(self):
		
		self.__ventana =Tk()
		self.__Frame=Frame()

		self.__ConstruyeVentana()

	def __ConstruyeVentana(self):
		
		#Titulo
		self.__ventana.title("Escaner De Puertos")
		self.__ventana.iconbitmap("Imagenes/reconocimiento.ico")
		self.__ventana.resizable(False,False)
		self.__ventana.geometry("700x400")
		self.__ventana.config(bg="#1D1C24")


		self.__Frame.pack()
		self.__Frame.config(bg="#292935")
		self.__Frame.config(width="600",height="300")


		self.__ventana.mainloop()



apli=Aplicacion()

