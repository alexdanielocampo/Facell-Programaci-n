from flask import Flask


def create_app():
    app = Flask(__name__)

    # Importamos el "blueprint" (grupo de rutas) de cada controlador
    from src.controllers.home_controller import home_bp
    from src.controllers.auth_controller import auth_bp
    from src.controllers.products_controller import products_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.suppliers_controller import suppliers_bp
    from src.controllers.sales_controller import sales_bp
    from src.controllers.users_controller import users_bp

    # Los registramos en la app para que Flask conozca las rutas
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(suppliers_bp)
    app.register_blueprint(sales_bp)
    app.register_blueprint(users_bp)

    return app
