import smtplib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from sqlqueries import QueriesSQLite

Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
	def __init__(self, poner_usuario_callback, **kwargs):
		super().__init__(*kwargs)
		self.poner_usuario=poner_usuario_callback

	def verificar_usuario(self, username, password):
		connection = QueriesSQLite.create_connection("pdvDB.sqlite")
		users=QueriesSQLite.execute_read_query(connection, "SELECT * from usuarios")
		if users:
			if username=='' or password=='':
				self.ids.signin_notificacion.text='Falta nombre de usuario y/o contraseña'
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
					if usuario['password']==password:
						print(usuario['username'])
						message = 'Se ha iniciado sesión en tu cuenta de FerreApp'
						subject = 'Mensaje de FerreApp'
						message = 'Subject: {}\n\n{}'.format(subject, message)
						server = smtplib.SMTP('smtp.gmail.com', 587)
						server.starttls()
						server.login('ferreapp980@gmail.com', 'yhrscvmtjmnghprx')
						server.sendmail('ferreapp980@gmail.com', usuario['username'], message.encode('utf-8'))
						server.quit()

						self.ids.username.text=''
						self.ids.password.text=''
						self.ids.signin_notificacion.text=''
						if usuario['tipo']=='trabajador':
							self.parent.parent.current='scrn_ventas'
						else:
							self.parent.parent.current='scrn_admin'
						self.poner_usuario(usuario)
					else:
						self.ids.signin_notificacion.text='Usuario o contraseña incorrecta'
				else:
					self.ids.signin_notificacion.text='Usuario inexistente'
		else:
			usuario_tuple=('usuario', 'Usuario Inicio', '123', 'admin')
			crear_usuario = "INSERT INTO usuarios (username, nombre, password, tipo) VALUES (?,?,?,?);"
			QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple)
			self.ids.signin_notificacion.text='Se creo primer usuario. usuario 123'

	def crear_usuario(self, username, password):
		connection = QueriesSQLite.create_connection("pdvDB.sqlite")
		users=QueriesSQLite.execute_read_query(connection, "SELECT * from usuarios")
		if users:
			if username=='' or password=='':
				self.ids.signin_notificacion.text='Falta nombre de usuario y/o contraseña'
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
						self.ids.signin_notificacion.text='El usuario ya existe'
				else:
					usuario_tuple=(username, 'Usuario prueba', password, 'admin')
					crear_usuario = "INSERT INTO usuarios (username, nombre, password, tipo) VALUES (?,?,?,?);"
					QueriesSQLite.execute_query(connection, crear_usuario, usuario_tuple)
					self.ids.signin_notificacion.text='Se creo el usuario'



class SigninApp(App):
	def build(self):
		return SigninWindow()

if __name__=="__main__":
	SigninApp().run()
