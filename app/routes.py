from flask import jsonify, Blueprint

dp = Blueprint('main', __name__)

@dp.route('/')
def home():
    return jsonify({"message": "Bem-vindo à API!"})