from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        # Validación básica: que no estén vacíos.
        if usuario == '' or clave == '':
            return render_template('login.html', error='Escribe tu usuario y tu contraseña.')

        return redirect(url_for('home.home'))

    return render_template('login.html', error=None)
