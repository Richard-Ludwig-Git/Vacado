from http.client import HTTPException
from typing import Annotated

import fastapi.exceptions
import pytest
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette import status
import backend.security
from .backend_endpoints import backapp

client = TestClient(backapp)

form = OAuth2PasswordRequestForm(
        username="string",
        password="string",
        scope="",
        grant_type="password"
        )

class Ueser(BaseModel):
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


def test_new_request_bad_user():
    response = client.post("/user_page/make_request", data={"duration":10,
                                                                "origin_city": "Berlin",
                                                                "transportation_type": "Car",
                                                                "max_travel_time": 8,
                                                                "theme": "Beach",
                                                                "accommodation": "Hotel",
                                                                "budget": 600,
                                                                "special_need": "Baby",
                                                                "current_user": form})
    print("response")
    assert response.status_code == 401
    #assert response.json() == {"detail": "Could not validate credentials"}






