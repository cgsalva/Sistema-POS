from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from application import db
from .models import Usuario

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods = ('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		usuario = Usuario.query.filter_by(username = username).first()

		if usuario:
			if check_password_hash(usuario.password, password):
				session.clear()
				session['id_usuario'] = usuario.id_usuario
			else:
				flash('Contraseña incorrecta')
		else:
			flash('Nombre de usuario incorrecto')

	return redirect('/')

@bp.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@bp.before_app_request
def load_logged_in_user():
	id_usuario = session.get('id_usuario')
	if id_usuario:
		g.usuario = Usuario.query.get_or_404(id_usuario)
	else:
		g.usuario = None

import functools

def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.usuario is None:
			return redirect(url_for('auth.login'))
		return view(**kwargs)
	return wrapped_view
