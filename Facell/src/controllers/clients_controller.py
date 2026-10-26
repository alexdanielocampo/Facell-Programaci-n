from flask import Blueprint, render_template

clients_bp = Blueprint('clients', __name__)


@clients_bp.route('/list_clients')
def list_clients():
    clientes = [
        {'nombre': 'Carlos Ocampo', 'documento': '7410216493', 'telefono': '300000000', 'compras': 15, 'estado': 'Activo', 'color': 'verde'},]
    return render_template(
        'clients/list_clients.html',
        clientes=clientes,
        total= 1,
        nuevos= 1,
        promedio='$0'
    )
# PROFE, MÁS ADELANTE DEBO CAMBIAR LO DE NUMERO DE CLIENTES Y ESAS COSA PARA QUE VAYA AUMENTANDO
# PROGRESIVAMENTE SEGÚN SE VAYAN AGREGANDO 
# TAMBIEN DEBO VOLVER FUNCIONAL LA BATTA DE BUSQUEDA Y EL ESTADO (ACTIVO O INNACTICO)