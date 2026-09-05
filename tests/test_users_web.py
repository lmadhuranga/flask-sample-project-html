def test_users_page(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert b"Users" in response.data
    assert b"Add User" in response.data


def test_create_user(client):
    response = client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"John Smith" in response.data
    assert b"john@example.com" in response.data
    assert b"User created successfully." in response.data


def test_create_user_duplicate_email(client):
    client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        }
    )

    response = client.post(
        "/users/create",
        data={
            "name": "Another User",
            "email": "john@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Email already exists." in response.data


def test_create_user_missing_name(client):
    response = client.post(
        "/users/create",
        data={
            "name": "",
            "email": "john@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Name and email are required." in response.data


def test_create_user_missing_email(client):
    response = client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": ""
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Name and email are required." in response.data


def test_edit_user(client, app):
    client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        }
    )

    with app.app_context():
        from models.user import User

        user = User.query.filter_by(
            email="john@example.com"
        ).first()

        user_id = user.id

    response = client.post(
        f"/users/{user_id}/edit",
        data={
            "name": "John Updated",
            "email": "john.updated@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"John Updated" in response.data
    assert b"john.updated@example.com" in response.data
    assert b"User updated successfully." in response.data


def test_edit_non_existing_user(client):
    response = client.get(
        "/users/999/edit",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"User not found." in response.data


def test_edit_user_duplicate_email(client):
    client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        }
    )

    client.post(
        "/users/create",
        data={
            "name": "Sarah Smith",
            "email": "sarah@example.com"
        }
    )

    response = client.post(
        "/users/2/edit",
        data={
            "name": "Sarah Updated",
            "email": "john@example.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Unable to update user. Email may already exist." in response.data


def test_delete_user(client, app):
    client.post(
        "/users/create",
        data={
            "name": "John Smith",
            "email": "john@example.com"
        }
    )

    with app.app_context():
        from models.user import User

        user = User.query.filter_by(
            email="john@example.com"
        ).first()

        user_id = user.id

    response = client.post(
        f"/users/{user_id}/delete",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"User deleted successfully." in response.data
    assert b"John Smith" not in response.data


def test_delete_non_existing_user(client):
    response = client.post(
        "/users/999/delete",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"User not found." in response.data


def test_users_pagination_first_page(client):
    for i in range(15):
        client.post(
            "/users/create",
            data={
                "name": f"User {i}",
                "email": f"user{i}@example.com"
            }
        )

    response = client.get("/users?page=1")

    assert response.status_code == 200

    # Newest users should appear first
    assert b"User 14" in response.data
    assert b"User 5" in response.data

    # User 4 should be on page 2
    assert b"User 4" not in response.data

    # Bootstrap pagination
    assert b"pagination" in response.data
    assert b"page-item active" in response.data
    assert b"Previous" in response.data
    assert b"Next" in response.data


def test_users_pagination_second_page(client):
    for i in range(15):
        client.post(
            "/users/create",
            data={
                "name": f"User {i}",
                "email": f"user{i}@example.com"
            }
        )

    response = client.get("/users?page=2")

    assert response.status_code == 200

    assert b"User 4" in response.data
    assert b"User 0" in response.data

    # Newest users should be on page 1
    assert b"User 14" not in response.data

    assert b"pagination" in response.data
    assert b"page-item active" in response.data