def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 302
    assert response.location.endswith("/users")


def test_users_page(client):
    response = client.get("/users")

    assert response.status_code == 200
    assert b"Users" in response.data


def test_create_user_page(client):
    response = client.get("/users/create")

    assert response.status_code == 200
    assert b"Create User" in response.data


def test_create_user_web(client):
    response = client.post(
        "/users/create",
        data={
            "name": "John",
            "email": "john@gmail.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"John" in response.data
    assert b"john@gmail.com" in response.data
    assert b"User created successfully." in response.data


def test_create_user_web_missing_name(client):
    response = client.post(
        "/users/create",
        data={
            "email": "john@gmail.com"
        }
    )

    assert response.status_code == 200
    assert b"Name and email are required." in response.data


def test_create_user_web_missing_email(client):
    response = client.post(
        "/users/create",
        data={
            "name": "John"
        }
    )

    assert response.status_code == 200
    assert b"Name and email are required." in response.data


def test_create_duplicate_user_web(client):
    client.post(
        "/users/create",
        data={
            "name": "John",
            "email": "john@gmail.com"
        }
    )

    response = client.post(
        "/users/create",
        data={
            "name": "David",
            "email": "john@gmail.com"
        }
    )

    assert response.status_code == 200
    assert b"Email already exists." in response.data


def test_edit_user_page(client):
    create_response = client.post(
        "/users/create",
        data={
            "name": "John",
            "email": "john@gmail.com"
        }
    )

    assert create_response.status_code == 302

    response = client.get("/users/1/edit")

    assert response.status_code == 200
    assert b"Edit User" in response.data
    assert b"John" in response.data


def test_edit_user_web(client):
    client.post(
        "/users/create",
        data={
            "name": "John",
            "email": "john@gmail.com"
        }
    )

    response = client.post(
        "/users/1/edit",
        data={
            "name": "John Updated",
            "email": "john.updated@gmail.com"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"John Updated" in response.data
    assert b"john.updated@gmail.com" in response.data
    assert b"User updated successfully." in response.data


def test_edit_user_not_found(client):
    response = client.get("/users/999/edit")

    assert response.status_code == 302
    assert response.location.endswith("/users")


def test_delete_user_web(client):
    client.post(
        "/users/create",
        data={
            "name": "John",
            "email": "john@gmail.com"
        }
    )

    response = client.post(
        "/users/1/delete",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"User deleted successfully." in response.data
    assert b"No users found." in response.data


def test_delete_user_not_found(client):
    response = client.post(
        "/users/999/delete",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"User not found." in response.data


def test_users_pagination(client):
    for i in range(25):
        client.post(
            "/users/create",
            data={
                "name": f"User {i}",
                "email": f"user{i}@gmail.com"
            }
        )

    response = client.get("/users?page=1")

    assert response.status_code == 200

    assert b"User 0" in response.data
    assert b"User 9" in response.data
    assert b"User 10" not in response.data

def test_users_pagination_page_two(client):
    for i in range(25):
        client.post(
            "/users/create",
            data={
                "name": f"User {i}",
                "email": f"user{i}@gmail.com"
            }
        )

    response = client.get("/users?page=2")

    assert response.status_code == 200

    assert b"User 10" in response.data
    assert b"User 19" in response.data
    assert b"User 0" not in response.data