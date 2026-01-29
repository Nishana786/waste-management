import os
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.report import Report
from app.repository.reportRepository import ReportRepository

UPLOAD_FOLDER = "uploads"

class ReportRouteHandler:

    @staticmethod
    def create_report():
        # 🧪 DEBUG — remove later
        print("AUTH:", request.headers.get("Authorization"))
        print("USER:", get_jwt_identity())
        print("FORM:", request.form)
        print("FILES:", request.files)

        # 🔐 logged-in user id
        user_id = int(get_jwt_identity())


        if not user_id:
            return jsonify({"message": "Invalid or missing token"}), 401

        # 📷 photo validation (SAFE)
        photo = request.files.get("photo")
        if not photo or photo.filename == "":
            return jsonify({"message": "Photo is required"}), 400

        # 📁 ensure uploads folder
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # 🔥 safe filename (avoid overwrite)
        filename = photo.filename
        photo.save(os.path.join(UPLOAD_FOLDER, filename))

        # 📝 create report
        report = Report(
            issueType=request.form.get("issueType"),
            description=request.form.get("description"),
            location=request.form.get("location"),
            photo=filename,
            user_id=user_id
        )

        ReportRepository.save(report)

        return jsonify({"message": "Report submitted successfully"}), 201
