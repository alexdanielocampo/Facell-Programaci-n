from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    # NUMEROS DE EJEMPLO PARA SIMULAR CÓMO SE VERÍA
    # MAS ADELANTE DEBO ORGANIZAR PARA QUE LA INFORMACIÓN SALGA DE LA DB.
    return render_template(
        'home.html',
        total_productos=125,
        total_proveedores=18,
        total_clientes=48,
        ventas_hoy=24
    )
