from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.routehandler.reportRouteHandler import ReportRouteHandler

report_bp = Blueprint("report", __name__)

# 🔓 Preflight
@report_bp.route("/report", methods=["OPTIONS"])
def report_options():
    return "", 200


# 🔐 Actual API 
@report_bp.route("/report", methods=["POST"])
@jwt_required()
def create_report():
    return ReportRouteHandler.create_report()
