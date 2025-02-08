from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)
app.config.from_object(Config)

def configure_db():
    """
    Configure MongoDB connection for both local and Heroku environments
    """
    # Get MongoDB URI from environment variable (Heroku) or use local default
    mongodb_uri = os.environ.get('MONGODB_URI')
    
    if mongodb_uri:
        # Parse username and password from mongodb_uri
        app.config['MONGODB_SETTINGS'] = {
            'host': mongodb_uri,
            'connect': True,
            'connectTimeoutMS': 30000,
            'socketTimeoutMS': 30000,
            'serverSelectionTimeoutMS': 30000
        }
    else:
        # Local development settings
        app.config['MONGODB_SETTINGS'] = {
            'db': 'UTA_Enrollment',  # Your local database name
            'host': 'localhost',
            'port': 27017
        }

# Initialize MongoDB
db = MongoEngine()
configure_db()
db.init_app(app)

# Import routes after db initialization to avoid circular imports
from application import routes

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)