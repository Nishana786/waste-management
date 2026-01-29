from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.routehandler.requestRouteHandler import RequestRouteHandler

request_bp = Blueprint("request", __name__)

# 🔓 Preflight
@request_bp.route("/request", methods=["OPTIONS"])
def request_options():
    return "", 200


# 🔐 Actual API
@request_bp.route("/request", methods=["POST"])
@jwt_required()
def create_request():
    return RequestRouteHandler.create_request()
