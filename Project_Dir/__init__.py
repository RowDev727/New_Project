from flask import Flask
from Project_Dir.config import Config
from Project_Dir.extensions import db, bcrypt, login_manager

def create_app(config_class=Config):
    # Initialize flask object
    app = Flask(__name__)
    
    # Set config object
    app.config.from_object(Config)
    
    # Initialize Apps
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    # Import Blueprints
    from Project_Dir.main.routes import main
    from Project_Dir.users.routes import users
    
    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(users)
    
    return app