from sqlalchemy.exc import IntegrityError

from extensions import db
from models.user import User


class UserService:
    """Service class responsible for user-related business logic."""

    def get_users(self):
        """
        Retrieve all users from the database.

        Returns:
            list: List of users represented as dictionaries.
        """
        users = User.query.all()

        return [user.to_dict() for user in users]

    def get_user(self, user_id):
        """
        Retrieve a user by ID.

        Args:
            user_id (int): ID of the user.

        Returns:
            dict | None: User data if found, otherwise None.
        """
        user = db.session.get(User, user_id)

        if not user:
            return None

        return user.to_dict()

    def create_user(self, name, email):
        """
        Create a new user.

        Args:
            name (str): User name.
            email (str): User email.

        Returns:
            dict | None: Created user or None if email already exists.
        """
        user = User(
            name=name,
            email=email
        )

        db.session.add(user)

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None

        return user.to_dict()

    def update_user(self, user_id, name, email):
        """
        Update an existing user.

        Args:
            user_id (int): ID of the user.
            name (str): New user name.
            email (str): New user email.

        Returns:
            dict | None: Updated user or None if not found/update failed.
        """
        user = db.session.get(User, user_id)

        if not user:
            return None

        user.name = name
        user.email = email

        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None

        return user.to_dict()

    def delete_user(self, user_id):
        """
        Delete a user from the database.

        Args:
            user_id (int): ID of the user.

        Returns:
            bool: True if deleted, otherwise False.
        """
        user = db.session.get(User, user_id)

        if not user:
            return False

        db.session.delete(user)
        db.session.commit()

        return True