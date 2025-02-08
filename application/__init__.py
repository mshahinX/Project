from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)
app.config.from_object(Config)

# Updated MongoDB Atlas configuration
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://shahin:memmedshahin12@cluster0.il8xc.mongodb.net/UTA_Enrollment',
    'connect': True,
    'tls': True,
    'tlsAllowInvalidCertificates': False,
    'retryWrites': True,
    'w': 'majority',
    'connectTimeoutMS': 30000,
    'socketTimeoutMS': 30000,
    'serverSelectionTimeoutMS': 30000
}

db = MongoEngine(app)

from application import routes

# Import routes after db initialization
from application import routes

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)