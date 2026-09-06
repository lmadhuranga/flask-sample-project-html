from flask import Blueprint, request, jsonify
from services.user_service import UserService


api_bp = Blueprint("api", __name__)
user_service = UserService()


@api_bp.route("/api", methods=["GET"])
def home():
    """
    Check the health status of the API.

    Returns:
        Response: JSON response indicating that the API is running.
        Status Code: 200
    """
    return jsonify({
        "health": "OK"
    }), 200


@api_bp.route("/api/users", methods=["GET"])
def users():
    """
    Retrieve a paginated list of users.

    Query Parameters:
        page (int): Page number. Defaults to 1.

    Returns:
        Response: JSON containing paginated user data.
        Status Code: 200
    """
    page = request.args.get("page", 1, type=int)

    pagination = user_service.get_users(
        page=page,
        per_page=10
    )

    return jsonify({
        "data": pagination
    }), 200


@api_bp.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Retrieve a single user by ID.

    Args:
        user_id (int): ID of the user.

    Returns:
        Response:
            User information if found.
            Error message if the user does not exist.

        Status Codes:
            200: User found.
            404: User not found.
    """
    user = user_service.get_user(user_id)

    if not user:
        return jsonify({
            "error": "User not found."
        }), 404

    return jsonify({
        "id": user_id,
        "name": user["name"],
        "email": user["email"]
    }), 200


@api_bp.route("/api/users", methods=["POST"])
def create_user():
    """
    Create a new user.

    Expected JSON:
        {
            "name": "John Smith",
            "email": "john@example.com"
        }

    Returns:
        Response:
            Success message and created user information.

        Status Codes:
            201: User created successfully.
            400: Invalid request data.
            409: Email already exists.
    """
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON request body is required."
        }), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({
            "error": "Name and email are required."
        }), 400

    user = user_service.create_user(name, email)

    if not user:
        return jsonify({
            "error": "Email already exists."
        }), 409

    return jsonify({
        "success": "User created successfully.",
        "data": user
    }), 201


@api_bp.route("/api/users/<int:user_id>", methods=["PUT"])
def edit_user(user_id):
    """
    Update an existing user.

    Args:
        user_id (int): ID of the user to update.

    Expected JSON:
        {
            "name": "John Updated",
            "email": "john.updated@example.com"
        }

    Returns:
        Response:
            Updated user information or an error message.

        Status Codes:
            200: User updated successfully.
            400: Invalid request data.
            404: User not found.
            409: Email already exists.
    """
    user = user_service.get_user(user_id)

    if not user:
        return jsonify({
            "error": "User not found."
        }), 404

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "JSON request body is required."
        }), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({
            "error": "Name and email are required."
        }), 400

    updated_user = user_service.update_user(
        user_id,
        name,
        email
    )

    if not updated_user:
        return jsonify({
            "error": "Unable to update user. Email may already exist."
        }), 409

    return jsonify({
        "success": "User updated successfully.",
        "data": updated_user
    }), 200


@api_bp.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user by ID.

    Args:
        user_id (int): ID of the user to delete.

    Returns:
        Response:
            Success message if deleted.
            Error message if the user does not exist.

        Status Codes:
            200: User deleted successfully.
            404: User not found.
    """
    deleted = user_service.delete_user(user_id)

    if not deleted:
        return jsonify({
            "error": "User not found."
        }), 404

    return jsonify({
        "success": "User deleted successfully."
    }), 200