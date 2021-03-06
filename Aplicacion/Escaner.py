#EXEPCION PARA LOS PAQUETES
try:
	#PAQUETES
	import nmap
	from tkinter import *
	import requests
	from pymongo import MongoClient
	from pymongo import errors

except ImportError:

	print("Hubo un problema importando alguno de los modulos")

class Aplicacion(nmap.PortScanner):


	#CONSTRUCTOR
	def __init__(self):



		try:

			#IMPORTANDO EL ERROR DE CONEXION FALLIDA
			raise errors.ConnectionFailure(message="hubo un problema para conectarse al servidor de la base de datos")

			#CREANDO LA CONEXION CON EL SERVIDOR
			Cliente=MongoClient("mongodb+srv://GabrielTiburon:wwwaaa12@cluster0practicas.8kyiy.mongodb.net/Notas?retryWrites=true&w=majority")

			#ACCEDIENDO A LA BASE DE DATOS
			self.__bd=Cliente['Notas']

			#ASIGNANDO LA CONEXION COMO Verdadera
			self.__conexion=True

		except errors.ConnectionFailure as test:

			#ASIGNANDO LA CONEXION COMO FALSA
			self.__conexion=False

			mensaje=test.args[0]

			#IMPRIMIENDO EL MENSAJE
			print(mensaje)

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

		#CREANDO LA BARRA DE TEXT AREA
		self.__barra=Scrollbar(self.__Frame4,command=self.__textoMostrar.yview)

		#CREANDO EL FORMULARIO DE DESCRIPCION BREVE DEL PANEL IZQUIERDO
		self.__descripcionBreve=Entry(self.__Frame2)

		#CREANDO EL TEXT AREA DE ESCRIBIR NOTA EN EL PANEL IZQUIERDO
		self.__nota=Text(self.__Frame2)

		#CREANDO EL BOTON DE ENVIAR LA NOTA EN EL PANEL IZQUIERDO
		self.__BotonE=Button(self.__Frame2)

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

	def __hacerEscaner(self):


		try:

			Escanear=self.scan(self.__ipFormulario.get(),self.__Puertos.get())

			for EquiposEscaneados in Escanear.all_hosts():

				self.__textoMostrar.insert(INSERT,"Ip:" + EquiposEscaneados + " /Estado:" + Escanear[EquiposEscaneados].state())

				#print("Ip:" + EquiposEscaneados + " /Estado:" + Escanear[EquiposEscaneados].state())

				if Escanear[EquiposEscaneados].state()=="down" or Escanear[EquiposEscaneados].state()=="unknown":

					self.__textoMostrar.insert(INSERT,"El host esta down no se escanean los puertos")

					#print("El host esta down no se escanean los puertos")

				elif Escanear[EquiposEscaneados].state()=="up":

					for Puerto in Escanear[EquiposEscaneados]["tcp"].keys():

						for datos in Escanear[EquiposEscaneados]["tcp"][Puerto]:
							self.__textoMostrar.insert(INSERT,"El puerto esta:" + datos["state"])
							#print(datos["state"])

		except:

			print("Hubo un problema al hacer el escaneo")

	def __enviarNota(self):
		#COMPROBANDO SI HAY CONEXION
		if self.__conexion:

			try:

				coleccionNotas=self.__db.notas

				datos = {"DescripcionBreve":self.__descripcionBreve.get(),"texto":self.__nota.get()}

				coleccionNotas.insert_one(datos).inserted_id

			except:

				print("hubo un error al enviar la nota")


		elif self.__conexion==False:

			print("No se puede enviar la nota debido a que no hay conexion con la base de datos")

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
		self.__BotonMac.config(text="Buscar",bg="#44AA2A",foreground="white", command=self.__hacerPeticion)

		#UBICACION DEL BOTON BUSCAR
		self.__BotonMac.place(x=150,y=50)

	def __ConstruyePanelInferior(self):

		self.__Frame4.pack(side="bottom",pady=10)
		self.__Frame4.config(bg="#292935",width="400",height="150")

		self.__ipFormulario.place(x=30,y=20)
		self.__ipFormulario.config(text="Mac-Address",bg="#1D1C24",foreground="white")
		self.__BotonEscaner.config(text="Empezar Escaneo",bg="#44AA2A",foreground="white",command=self.__hacerEscaner)
		self.__BotonEscaner.place(x=30,y=100)

		self.__textoMostrar.place(x=165,y=9)
		self.__textoMostrar.config(bg="#1D1C24",width=28,height=8,foreground="white")
		self.__Puertos.config(bg="#1D1C24",foreground="white")
		self.__Puertos.place(x=30,y=60)
		self.__barra.place(x=375,y=9)


	def __ConstruyePanelIzquierdo(self):

		#FRAME IZQUIERDO UBICACION Y MARGEN
		self.__Frame2.pack(side="left",pady=10)
		#FRAME COLOR DE FONDO Y TAMAÑO
		self.__Frame2.config(bg="#292935",width="140",height="400")

		#FORMULARIO DE DESCRIPCION BREVE COLOR DE FONDO Y DE LETRA
		self.__descripcionBreve.config(bg="#1D1C24",foreground="white")
		#FORMULARIO DE DESCRIPCION BREVE UBICACION
		self.__descripcionBreve.place(x=7,y=20)

		#FORMULARIO DE NOTA COLOR DE FONDO TAMAÑO Y COLOR DE LETRA
		self.__nota.config(bg="#1D1C24",width=15,height=16,foreground="white")
		#UBICACION DEL FORMULARIO NOTA
		self.__nota.place(x=7,y=50)

		#BOTON DE ENVIAR DEL PANEL IZQUIERDO TEXTO COLOR DE FONDO Y DE LETRA
		self.__BotonE.config(text="Enviar",bg="#44AA2A",foreground="white",command=self.__enviarNota)
		#UBICACION DEL BOTON ENVIAR
		self.__BotonE.place(x=46,y=330)


	def __ConstruyePanelDerecho(self):

		self.__Frame3.pack(side="right")
		self.__Frame3.config(bg="#292935",width="100",height="400")



A=Aplicacion()
