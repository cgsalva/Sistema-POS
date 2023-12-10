from flask import Blueprint, render_template, request, url_for, redirect, flash, jsonify
from application import db
from application.auth import login_required
from .models import Categoria

bp = Blueprint('categorias', __name__, url_prefix='/productos/categorias')

@bp.route('/')
@login_required
def index():
	return render_template('categorias/index.html')
