from app.models.report import Report
from app.extensions import db

class ReportRepository:

    @staticmethod
    def save(report):
        db.session.add(report)
        db.session.commit()

    @staticmethod
    def count_by_user(user_id):
        return Report.query.filter_by(user_id=user_id).count()

    @staticmethod
    def find_all():
        return Report.query.all()
    
