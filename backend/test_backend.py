from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
from pydantic import BaseModel
import backend.security
from .backend_endpoints import backapp
from .security import security_router


backapp.include_router(security_router)
client = TestClient(backapp)


form = OAuth2PasswordRequestForm(
        username="string",
        password="string",
        scope="",
        grant_type="password"
        )

class User(BaseModel):
    user_id: int
    user_name: str
    email: str


def test_create_user():
    response = client.post("/onboarding",  data={"username": "Testuser1", "password": "hey", "email": "lolamail"})
    assert response.status_code == 201


def test_create_user_field_empty():
    response = client.post("/onboarding",  data={"username": "", "password": "hey", "email": "lolamail"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Required filed not given"}


def test_new_request_all_correct():
    token = backend.security.create_access_token(data={"sub": "string"})
    response = client.post("/user_page/make_request", data={"duration":10,
                                                                "origin_city": "Berlin",
                                                                "transportation_type": "Car",
                                                                "max_travel_time": 9,
                                                                "theme": "Beach",
                                                                 "accommodation": "Hotel",
                                                                 "budget": 600,
                                                                 "special_need": "Baby"}
                                                                 , headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


def test_get_vacation_correct_user():
    token = backend.security.create_access_token(data={"sub": "string"})
    response = client.get("/user_page/show_vacations", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


def test_get_vacation_wrong_user():
    response = client.get("/user_page/show_vacations", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
    body = response.json()
    assert "detail" in body


def test_delete_response_success():
    token = backend.security.create_access_token(data={"sub": "string"})
    response = client.delete("/user_page/delete_response/?response_id=40",   headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200


def test_change_request_all_correct():
    token = backend.security.create_access_token(data={"sub": "string"})
    response = client.post(url="/user_page/make_request", data={"request_id": 39,
                                                                "duration":15,
                                                                "origin_city": "",
                                                                "transportation_type": "",
                                                                "max_travel_time": 0,
                                                                "theme": "",
                                                                 "accommodation": "",
                                                                 "budget": 0,
                                                                 "special_need": ""}
                                                                 , headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

"""SECURITY STUFF"""

def test_verif_pw_correct():
    assert backend.security.verify_pw("string", "$2b$12$7/U8d16NqlO9WDzg.JAA..6dkpfJBLzujBpnQwRLm8yXmqbzLsg8y") == True


def test_verif_pw_false():
    assert backend.security.verify_pw("stringwrong", "$2b$12$7/U8d16NqlO9WDzg.JAA..6dkpfJBLzujBpnQwRLm8yXmqbzLsg8y") == False


def test_authenticate_correct():
    assert backend.security.authenticate(username="string", real_pw="string") == backend.security.UserInDB(user_id=13, user_name='string', email='string', hashed_password='$2b$12$7/U8d16NqlO9WDzg.JAA..6dkpfJBLzujBpnQwRLm8yXmqbzLsg8y')


def test_authenticate_user_not_found():
    assert backend.security.authenticate(username="wrongguy", real_pw="test") == False


def test_authenticate_password_wrong():
    assert backend.security.authenticate(username="string", real_pw="test") == False


def test_create_access_token_correct_length():
    assert len(backend.security.create_access_token(data={"sub":"string"}, expires_delta=timedelta(minutes=30))) == 125


def test_get_current_user_correct():
    token = backend.security.create_access_token(data={"sub": "string"})
    assert backend.security.get_current_user(token) == backend.security.UserInDB(user_id=13, user_name='string', email='string', hashed_password='$2b$12$7/U8d16NqlO9WDzg.JAA..6dkpfJBLzujBpnQwRLm8yXmqbzLsg8y')


def test_login_success():
    response = client.post("/token", data={"username": "string", "password": "string", "scope":"",
        "grant_type": "password"})
    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"


def test_login_user_not_found():
    response = client.post("/token", data={"username": "string", "password": "wrong", "scope":"",
        "grant_type": "password"})
    assert response.status_code == 401
    body = response.json()
    assert body["detail"] == "User not found"
