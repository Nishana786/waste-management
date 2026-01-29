from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.request import PickupRequest
from app.repository.requestRepository import RequestRepository

class RequestRouteHandler:

    @staticmethod
    def create_request():
        user_id = int(get_jwt_identity())

        data = request.get_json()

        if not data:
            return jsonify({"message": "Invalid request"}), 400

        req = PickupRequest(
            address=data["address"],
            wasteType=data["wasteType"],
            date=data["date"],
            timeSlot=data["timeSlot"],
            phone=data["phone"],
            user_id=user_id
        )

        RequestRepository.save(req)
        return jsonify({"message": "Pickup request submitted"}), 201
