import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'[K\xeb\xcc\xf9\x14@\xbf\x17\xcb;\xd4LL\xe1\x80"

    MONGODB_HOST = 'mongodb+srv://shahin:memmedshahin12@cluster0.il8xc.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority'

