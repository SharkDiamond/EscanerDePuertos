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
		self.__ConstruyeVentana()


	def __ConstruyeVentana(self):

		#Titulo
		self.__ventana.title("Escaner De Puertos")
		self.__ventana.iconbitmap("Imagenes/reconocimiento.ico")
		self.__ventana.resizable(False,False)
		self.__ventana.geometry("700x400")
		self.__ventana.config(bg="#1D1C24")

		self.__Frame2.pack(side="left")
		self.__Frame2.config(bg="#292935",width="100",height="400")

		self.__Frame3.pack(side="right")
		self.__Frame3.config(bg="#292935",width="100",height="400")

		self.__Frame.pack(pady=10)
		self.__Frame.config(bg="#292935",width="400",height="150")

		self.__Frame4.pack(side="bottom",pady=10)
		self.__Frame4.config(bg="#292935",width="400",height="150")



		self.__Mac.place(x=150,y=20)
		self.__Label.place(x=150,y=60)
		self.__Label.config(text="Mac-Address")
		self.__ventana.mainloop()



apli=Aplicacion()
