from flask import Flask
from Models.model import *



app=Flask(__name__)

app.config['SECRET_KEY']="EAST"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gs.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# app.config['SQLALCHEMY_SILENCE_UBER_WARNING']=1



db.init_app(app)


with app.app_context():
    db.create_all()
    
    


