from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from services.user_service import UserService


web_bp = Blueprint("web", __name__)

user_service = UserService()

@web_bp.route("/")
def home():
    """
    Redirect the home page to the user list.
    """
    return redirect(url_for("web.users"))

@web_bp.route("/users")
def users():
    page = request.args.get("page", 1, type=int)

    pagination = user_service.get_users(
        page=page,
        per_page=2
    )

    return render_template(
        "users/list.html",
        users=pagination["users"],
        pagination=pagination
    )

@web_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    """Display and process the create-user form."""

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            flash("Name and email are required.", "error")
            return render_template("users/create.html")

        user = user_service.create_user(name, email)

        if not user:
            flash("Email already exists.", "error")
            return render_template("users/create.html")

        flash("User created successfully.", "success")

        return redirect(url_for("web.users"))

    return render_template("users/create.html")


@web_bp.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def edit_user(user_id):
    """Display and process the edit-user form."""

    user = user_service.get_user(user_id)

    if not user:
        flash("User not found.", "error")
        return redirect(url_for("web.users"))

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            flash("Name and email are required.", "error")

            return render_template(
                "users/edit.html",
                user=user
            )

        updated_user = user_service.update_user(
            user_id,
            name,
            email
        )

        if not updated_user:
            flash("Unable to update user. Email may already exist.", "error")

            return render_template(
                "users/edit.html",
                user=user
            )

        flash("User updated successfully.", "success")

        return redirect(url_for("web.users"))

    return render_template(
        "users/edit.html",
        user=user
    )


@web_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """Delete a user."""

    deleted = user_service.delete_user(user_id)

    if not deleted:
        flash("User not found.", "error")
    else:
        flash("User deleted successfully.", "success")

    return redirect(url_for("web.users"))