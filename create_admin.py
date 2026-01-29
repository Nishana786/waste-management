from app import create_app
from app.extensions import db, bcrypt
from app.models.user import User

app = create_app()

with app.app_context():
    user = User.query.filter_by(email="admin@gmail.com").first()

    if not user:
        user = User(
            name="Admin",
            email="admin@gmail.com",
            role="admin",
            password=bcrypt.generate_password_hash("admin123").decode("utf-8")
        )
        db.session.add(user)
    else:
        user.password = bcrypt.generate_password_hash("admin123").decode("utf-8")
        user.role = "admin"

    db.session.commit()
    print("✅ admin password RESET DONE")
