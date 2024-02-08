from tests.conftest import client

def test_create_user(client):
    response = client.post("http://127.0.0.1:5000/Users", json={'name': 'Moustafa', 'email': 'email@gmail.com', 'password': 'pass'})
    assert response.status_code == 200

def test_get_users(client):
    response = client.get("http://127.0.0.1:5000/Users")
    assert response.status_code == 200

def test_get_user(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={'name': 'Moustafa', 'email': 'email@gmail.com', 'password': 'pass'})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.get("http://127.0.0.1:5000/User?email=email@gmail.com", headers=headers)
    assert response.status_code == 200

def test_update_user(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={"name": "Moustafa", "email": "email@gmail.com", "password": "pass"})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.put("http://127.0.0.1:5000/User", headers=headers, json = {"email": "email@gmail.com", "name": "lily"})
    assert response.status_code == 200

def test_delete_user(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={"name": "Moustafa", "email": "email@gmail.com", "password": "pass"})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.delete("http://127.0.0.1:5000/User?email=email@gmail.com", headers=headers)
    assert response.status_code == 200

def test_delete_users(client):
    response = client.delete("http://127.0.0.1:5000/Users")
    assert response.status_code == 200

def test_create_user_invalid(client):
    response = client.post("http://127.0.0.1:5000/Users", json={'email': 'email@gmail.com', 'password': 'pass'})
    assert response.status_code == 400

def test_create_user_exists(client):
    response = client.post("http://127.0.0.1:5000/Users", json={'name': 'Moustafa', 'email': 'email@gmail.com', 'password': 'pass'})
    response = client.post("http://127.0.0.1:5000/Users", json={'name': 'Yousef', 'email': 'email@gmail.com', 'password': 'pass'})
    assert response.status_code == 401

def test_get_user_invalid(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={'name': 'Moustafa', 'email': 'email@gmail.com', 'password': 'pass'})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.get("http://127.0.0.1:5000/User?emai=email@gmail.com", headers=headers)
    assert response.status_code == 400

def test_get_user_missing(client, jwt_token):
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.get("http://127.0.0.1:5000/User?email=email@gmail.com", headers=headers)
    assert response.status_code == 404

def test_update_user_invalid(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={"name": "Moustafa", "email": "email@gmail.com", "password": "pass"})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.put("http://127.0.0.1:5000/User", headers=headers, json = {"email": "email@gmail.com", "na": "lily"})
    assert response.status_code == 400

def test_update_user_missing(client, jwt_token):
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.put("http://127.0.0.1:5000/User", headers=headers, json = {"email": "email@gmail.com", "name": "lily"})
    assert response.status_code == 404

def test_delete_user_invalid(client, jwt_token):
    response = client.post("http://127.0.0.1:5000/Users", json={"name": "Moustafa", "email": "email@gmail.com", "password": "pass"})
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.delete("http://127.0.0.1:5000/User?ema=email@gmail.com", headers=headers)
    assert response.status_code == 400

def test_delete_user_missing(client, jwt_token):
    headers = {"Authorization" : f"Bearer {jwt_token}"}
    response = client.delete("http://127.0.0.1:5000/User?email=email@gmail.com", headers=headers)
    assert response.status_code == 404