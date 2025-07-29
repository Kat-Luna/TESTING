from flask import Flask
from models import init_db
from routes.user import user_bp
from routes.scan import scan_bp
from routes.certificate import certificate_bp  # Ensure this file & route exist

def create_app():
    app = Flask(__name__)
    
    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wsacp.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'your_secret_key_here'  # Change this in production

    # Initialize DB
    init_db(app)

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(scan_bp)
    app.register_blueprint(certificate_bp)

    return app

# Entry point
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
