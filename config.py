import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_HOST = 'mongodb+srv://shahin:memmedshahin12@cluster0.il8xc.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority'

