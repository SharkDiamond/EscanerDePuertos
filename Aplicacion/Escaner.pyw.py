from nmap.nmap import PortScanner
from tkinter import *


class Aplicacion(PortScanner):
	

	def __init__(self):
		
		self.__ventana = Tk()
		self.__ConstruyeVentana()

	def __ConstruyeVentana(self):
		#Titulo
		self.__ventana.title("Escaner De Puertos")
		self.__ventana.iconbitmap("Imagenes/reconocimiento.ico")
		self.__ventana.resizable(False,False)
		self.__ventana.geometry("700x400")
		self.__ventana.config(bg="black")
		self.__ventana.mainloop()



apli=Aplicacion()

