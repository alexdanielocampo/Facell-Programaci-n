from flask import Blueprint, render_template

users_bp = Blueprint('users', __name__)


@users_bp.route('/list_users')
def list_users():
    return render_template('en_construccion.html', titulo='USUARIOS', icono='bi-person-circle')

# Espero explicación del profe para ver como es la autenticación
# Creo que necesito la base de datos para validar información 