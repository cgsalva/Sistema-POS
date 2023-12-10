from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_mapping(
	DEBUG = True,
	SECRET_KEY = 'dev',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///posdb.db'
)

db.init_app(app)

from . import auth, categorias

app.register_blueprint(auth.bp)
app.register_blueprint(categorias.bp)

@app.route('/')
def index():
	if g.usuario:
		return render_template('index.html')
	else:
		return render_template('auth/login.html')

with app.app_context():
	db.create_all()
