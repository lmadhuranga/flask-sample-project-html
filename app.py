from flask import Flask
from flasgger import Swagger
from extensions import db 
from routes.web_routes import web_bp
from routes.api_routes import api_bp
from seed import seed_fake_users

def create_app(test_config=None):
    """
    Create and configure the Flask application.

    Args:
        test_config (dict, optional):
            Configuration values used primarily for testing.

    Returns:
        Flask:
            Configured Flask application instance.
    """

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
 
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    Swagger(app)

    with app.app_context():
        db.create_all()
        seed_fake_users()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5001)