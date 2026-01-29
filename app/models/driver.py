
from app.extensions import db

class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False, unique=True)

    vehicle_number = db.Column(db.String(50), nullable=False)
    area = db.Column(db.String(100), nullable=False)

    status = db.Column(
        db.String(20),
        default="available"  
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Driver {self.name}>"
