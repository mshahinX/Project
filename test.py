from mongoengine import connect
from mongoengine.connection import get_db

# Test connection
connect(host='mongodb+srv://shahin:memmedshahin12@cluster0.il8xc.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority')
db = get_db()
print("Connected to:", db.name)