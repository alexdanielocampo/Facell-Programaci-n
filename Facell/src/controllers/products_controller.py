from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__)


@products_bp.route('/list_products')
def list_products():
    # PRODUCTO AGREGADO DE EJEMPLO.
    productos = [
        {'nombre': 'Vidrio templado', 'categoria': 'Cuidado', 'precio': '$ 15.000', 'stock': 98, 'estado': 'Disponible', 'color': 'verde'},
    ]

    return render_template(
        'products/list_products.html',
        productos=productos,
        total=125,
        bajos=18,
        valor='$ 4.000'
    )
# MÁS ADELANTE DEBO VOLVER FUNCIONAL LA BARRA DE BUSQUEDA Y LAS CATEGORÍAS