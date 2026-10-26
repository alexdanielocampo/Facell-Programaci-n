from flask import Blueprint, render_template

sales_bp = Blueprint('sales', __name__)


@sales_bp.route('/list_sales')
def list_sales():
    return render_template('en_construccion.html', titulo='VENTAS', icono='bi-graph-up')

# Espero la explicación del profe 