import smtplib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from sqlqueries import QueriesSQLite

Builder.load_file('signin/signup.kv')

class SignupWindow(BoxLayout):
	def __init__(self, poner_usuario_callback, **kwargs):
		super().__init__(*kwargs)
		self.poner_usuario=poner_usuario_callback

	def Regresar(self):
		self.parent.parent.current='scrn_signin'

	def crear_usuario(self, username, password, correo, tipo, name):
		connection = QueriesSQLite.create_connection("pdvDB.sqlite")
		users=QueriesSQLite.execute_read_query(connection, "SELECT * from usuarios")
		if users:
			if username=='' or password=='':
				self.ids.signup_notificacion.text='Falta nombre de usuario y/o contraseña'
			else:
				usuario={}
				for user in users:
					if user[0]==username:
						usuario['nombre']=user[1]
						usuario['username']=user[0]
						usuario['password']=user[2]
						usuario['tipo']=user[3]
						break
				if usuario:
						self.ids.signup_notificacion.text='El usuario ya existe'
				else:
					usuario_tuple=(username, name, password, tipo, correo)
					crear_usuario = "INSERT INTO usuarios (username, nombre, password, tipo, correo) VALUES (?,?,?,?,?);"
					QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple)
					self.ids.signup_notificacion.text='Se creo el usuario'
					self.parent.parent.current='scrn_signin'



class SignupApp(App):
	def build(self):
		return SignupWindow()

if __name__=="__main__":
	SignupApp().run()
