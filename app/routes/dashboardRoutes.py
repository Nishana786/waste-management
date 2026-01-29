from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.routehandler.dashboardRouteHandler import DashboardRouteHandler

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard/stats", methods=["GET"])
@jwt_required()
def dashboard_stats():
    return DashboardRouteHandler.get_stats()
