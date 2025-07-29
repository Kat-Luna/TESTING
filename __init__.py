from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the database instance
db = SQLAlchemy()

def init_db(app):
    """
    Initializes the database with the Flask application context.
    Creates all tables if they don't exist and ensures wsacp.db is created.
    """
    db_path = os.path.join(os.getcwd(), 'wsacp.db')
    print(f"🧠 Database path: {db_path}")

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    db.init_app(app)

    # Import all models here to register them before creating tables
    from models.user import User
    from models.audit import AuditResult
    from models.certificate import Certificate

    with app.app_context():
        db.create_all()
        print("✅ Database initialized and tables created successfully.")
