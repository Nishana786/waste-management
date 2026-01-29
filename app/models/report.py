from datetime import datetime
from app.extensions import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issueType = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    photo = db.Column(db.String(200))
    status = db.Column(db.String(50), default="pending")
    user_id = db.Column(db.Integer)

    timeSlot = db.Column(db.String(50), nullable=True)

    notification_sent = db.Column(db.Boolean, default=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
