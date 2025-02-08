import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    MONGODB_HOST = 'mongodb+srv://shahin:<your_actual_password>@cluster0.il8xc.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority'
    
# __init__.py
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)
app.config.from_object(Config)

# Configure MongoDB Atlas connection
app.config['MONGODB_SETTINGS'] = {
    'host': app.config['MONGODB_HOST'],
    'connect': True,
    'connectTimeoutMS': 30000,
    'socketTimeoutMS': 30000,
    'serverSelectionTimeoutMS': 30000
}

# Initialize MongoDB
db = MongoEngine()
db.init_app(app)

# Import routes after db initialization
from application import routes

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)