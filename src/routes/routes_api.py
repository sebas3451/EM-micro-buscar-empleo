from flask import Blueprint, request, jsonify
from utils.db import db
from models.model import OfertaEmpleo

routes_api = Blueprint('routes_api',__name__)

@routes_api.route('/prueba')
def prueba():
    try:
        return dict(success='ok')
    except Exception as e:
        print(e)
        return {'success':False, 'message':str(e)}