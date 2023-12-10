from application import db

class Usuario(db.Model):
	__tablename__ = 'usuario'

	id_usuario = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	password = db.Column(db.Text, nullable = False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return f'<Usuario: {self.username}>'

class Categoria(db.Model):
	__tablename__ = 'categoria'

	id_categoria = db.Column(db.Integer, primary_key = True)
	nombre = db.Column(db.String(50), unique = True, nullable = False)
	descripcion = db.Column(db.Text, nullable = False)

	def __init__(self, nombre, descripcion):
		self.nombre = nombre
		self.descripcion = descripcion

	def __repr__(self):
		return f'<Categoria: {self.nombre}>'

class Unidad(db.Model):
	__tablename__ = 'unidad'

	id_unidad = db.Column(db.Integer, primary_key = True)
	nombre = db.Column(db.String(50), unique = True, nullable = False)
	nombre_corto = db.Column(db.String(10), unique = True, nullable = False)

	def __init__(self, nombre, nombre_corto):
		self.nombre = nombre
		self.nombre_corto = nombre_corto

	def __repr__(self):
		return f'<Unidad: {self.nombre} ({self.nombre_corto})>'