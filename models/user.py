from extensions import db


class User(db.Model):
    """Database model representing a user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    def to_dict(self):
        """Convert the user model to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }