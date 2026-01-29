from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from app.routehandler.driver_route_handler import DriverRouteHandler

driver_bp = Blueprint("driver_bp", __name__)


def is_admin():
    claims = get_jwt()
    return claims.get("role") == "admin"


# ✅ ADD DRIVER (ADMIN ONLY)
@driver_bp.route("/admin/drivers", methods=["POST"])
@jwt_required()
def add_driver():
    if not is_admin():
        return jsonify({"message": "Admin only"}), 403

    driver = DriverRouteHandler.add_driver(request.json)
    return jsonify({"message": "Driver added", "id": driver.id}), 201


# ✅ GET ALL DRIVERS (ADMIN ONLY)
@driver_bp.route("/admin/drivers", methods=["GET"])
@jwt_required()
def get_drivers():
    if not is_admin():
        return jsonify({"message": "Admin only"}), 403

    drivers = DriverRouteHandler.get_drivers()
    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "phone": d.phone,
            "vehicle_number": d.vehicle_number,
            "area": d.area,
            "status": d.status
        } for d in drivers
    ]), 200


# 🗑️ DELETE DRIVER (ADMIN ONLY)
@driver_bp.route("/admin/drivers/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_driver(id):
    if not is_admin():
        return jsonify({"message": "Admin only"}), 403

    DriverRouteHandler.delete_driver(id)
    return jsonify({"message": "Driver deleted"}), 200


# ✅ MARK DRIVER COMPLETED
@driver_bp.route("/admin/drivers/<int:id>/complete", methods=["PUT"])
@jwt_required()
def complete_driver(id):
    if not is_admin():
        return jsonify({"message": "Admin only"}), 403

    DriverRouteHandler.complete_driver(id)
    return jsonify({"message": "Driver marked completed"}), 200

@driver_bp.route("/admin/drivers/<int:id>/assign", methods=["PUT"])
@jwt_required()
def assign_driver(id):
    if not is_admin():
        return jsonify({"message": "Admin only"}), 403

    DriverRouteHandler.assign_driver(id)
    return jsonify({"message": "Driver assigned"}), 200


   
