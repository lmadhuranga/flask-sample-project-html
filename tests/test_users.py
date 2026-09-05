def test_get_users(client):
  response = client.get("/users")

  assert response.status_code ==200
  assert response.json==[]


def test_create_user(client):
  response = client.post(
    "/users",
    json={
      "name":"John",
      "email":"john@gmail.com"
    }
  )

  assert response.status_code - 201

  data = response.json

  assert data['name'] == "John"
  assert data['email'] == "john@gmail.com"
  assert "id" in data


def test_get_user(client):
  create_response = client.post(
    "/users",
    json={
      "name":"John",
      "email":'john@gmail.com'
    }
  )

  user_id = create_response.json['id']

  response = client.get(f"/users/{user_id}")

  assert response.status_code == 200

  assert  response.json['name'] == "John"


def test_update_user(client):
  create_response = client.post(
    "/users",
    json={
      "name":"John",
      "email":'john@gmail.com'
    }
  )

  user_id = create_response.json['id']

  response = client.put(
      f"/users/{user_id}",
      json={
          "name": "John Updated",
          "email": "john.updated@example.com"
      }
  )

  assert response.status_code == 200
  assert response.json["name"] == "John Updated"
  assert response.json["email"] == "john.updated@example.com"

def test_delete_user(client):
    create_response = client.post(
        "/users",
        json={
            "name": "John",
            "email": "john@example.com"
        }
    )

    user_id = create_response.json["id"]

    response = client.delete(f"/users/{user_id}")

    assert response.status_code == 200

    response = client.get(f"/users/{user_id}")

    assert response.status_code == 404

def test_create_user_without_name(client):
    response = client.post(
        "/users",
        json={
            "email": "john@example.com"
        }
    )

    assert response.status_code == 400

def test_create_user_invalid_email(client):
    response = client.post(
        "/users",
        json={
            "name": "John",
            "email": "invalid-email"
        }
    )

    assert response.status_code == 400

def test_duplicate_email(client):

    client.post(
        "/users",
        json={
            "name": "John",
            "email": "john@example.com"
        }
    )

    response = client.post(
        "/users",
        json={
            "name": "David",
            "email": "john@example.com"
        }
    )

    assert response.status_code == 409