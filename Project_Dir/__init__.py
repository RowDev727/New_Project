from flask import Flask
from Project_Dir.config import Config

def create_app(config_class=Config):
    # Initialize flask object
    app = Flask(__name__)
    
    # Set config object
    app.config.from_object(Config)
    
    # Import Blueprints
    from Project_Dir.main.routes import main
    
    # Register Blueprints
    app.register_blueprint(main)    
    
    return app