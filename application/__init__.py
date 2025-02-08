from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
import os
app = Flask(__name__)
app.config.from_object(Config)


db = MongoEngine()
db.init_app(app)

from application import routes

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
