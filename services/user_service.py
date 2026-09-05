from sqlalchemy.exc import IntegrityError

from extensions import db
from models.user import User


class UserService:
    """Service layer responsible for user-related business operations."""

    def get_users(self, page=1, per_page=10):
        """
        Retrieve a paginated list of users.

        Args:
            page (int): The page number to retrieve.
            per_page (int): Number of users to return per page.

        Returns:
            dict: Pagination information and the list of users.
        """
        pagination = User.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )

        return {
            "users": [user.to_dict() for user in pagination.items],
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
            "next_num": pagination.next_num,
            "prev_num": pagination.prev_num,
        }

    def get_user(self, user_id):
        """
        Retrieve a single user by ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            dict | None: User data if the user exists, otherwise None.
        """
        user = db.session.get(User, user_id)

        if not user:
            return None

        return user.to_dict()

    def create_user(self, name, email):
        """
        Create a new user.

        Args:
            name (str): The user's name.
            email (str): The user's email address.

        Returns:
            dict | None: Created user data if successful,
            otherwise None when the email already exists.
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
            user_id (int): The ID of the user to update.
            name (str): The updated user name.
            email (str): The updated email address.

        Returns:
            dict | None: Updated user data if successful,
            otherwise None if the user does not exist or
            the email already exists.
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
        Delete a user by ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted,
            otherwise False if the user does not exist.
        """
        user = db.session.get(User, user_id)

        if not user:
            return False

        db.session.delete(user)
        db.session.commit()

        return True