from extensions import db
from models.user import User


def seed_fake_users():
    """Create fake users if the database is empty."""

    if User.query.count() > 0:
        return

    fake_users = [
        ("John Smith", "john.smith@example.com"),
        ("Sarah Johnson", "sarah.johnson@example.com"),
        ("Michael Brown", "michael.brown@example.com"),
        ("Emily Davis", "emily.davis@example.com"),
        ("David Wilson", "david.wilson@example.com"),
        ("Jessica Taylor", "jessica.taylor@example.com"),
        ("Daniel Anderson", "daniel.anderson@example.com"),
        ("Sophia Thomas", "sophia.thomas@example.com"),
        ("James Jackson", "james.jackson@example.com"),
        ("Olivia White", "olivia.white@example.com"),
        ("Robert Harris", "robert.harris@example.com"),
        ("Emma Martin", "emma.martin@example.com"),
        ("William Thompson", "william.thompson@example.com"),
        ("Ava Garcia", "ava.garcia@example.com"),
        ("Christopher Martinez", "christopher.martinez@example.com"),
    ]

    for name, email in fake_users:
        user = User(
            name=name,
            email=email
        )

        db.session.add(user)

    db.session.commit()