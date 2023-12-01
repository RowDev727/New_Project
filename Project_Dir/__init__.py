from flask import Flask
from .config import Config
from .extensions import bcrypt, db, login_manager
from .models import User, Post

def create_app(config_class=Config):
    # Initialize flask object
    app = Flask(__name__)
    
    # Set config object
    app.config.from_object(Config)
    
    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Import Blueprints
    from Project_Dir.main.routes import main
    from Project_Dir.users.routes import users
    
    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(users)
    
    # Required application context for database creation
    with app.app_context():
        db.create_all()
    
    return app