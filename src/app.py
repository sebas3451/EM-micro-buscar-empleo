from flask import Flask, request
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
from routes.routes_api import routes_api
# from config import DATABASE_CONNECTION_URI


app = Flask(__name__)

#datos para conectar con la db

# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy(app)

CORS(app)

app.register_blueprint(routes_api)