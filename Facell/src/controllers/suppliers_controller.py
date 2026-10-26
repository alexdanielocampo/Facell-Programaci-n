from flask import Blueprint, render_template

suppliers_bp = Blueprint('suppliers', __name__)
 
 # LISRA DE EJEMPLO 
@suppliers_bp.route('/list_suppliers')
def list_suppliers():
    proveedores = [
        {'nombre': 'Carlos Ocampo', 'empresa': 'Kaché', 'telefono': '300000000', 'saldo': '0', 'estado': 'Al día', 'color': 'verde'},
        {'nombre': 'Pepito Pérez', 'empresa': 'Mundo Movi', 'telefono': '3011111111', 'saldo': '0', 'estado': 'Al día', 'color': 'verde'},
        {'nombre': 'Jorge Ballesteros', 'empresa': 'MoviCel', 'telefono': '302222222', 'saldo': '0', 'estado': 'Al día', 'color': 'verde'},
        {'nombre': 'Alex Sierra', 'empresa': 'Kaché', 'telefono': '305555555', 'saldo': '$ 254.000', 'estado': 'Pendiente', 'color': 'rojo'},
    ]

    return render_template(
        'suppliers/list_suppliers.html',
        proveedores=proveedores,
        total=12,
        pendientes=3,
        por_pagar='$ 254.000'
    )
# DEBO HACER FUNCIONAL LA BARRA DE BUSQUEDA Y LAS CATEGORÍAS 