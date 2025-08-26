from fastapi import APIRouter, Form
from backend import data_handling, security, openai_communication
from fastapi.responses import RedirectResponse
from fastapi.params import Depends
from pydantic import BaseModel
import asyncio

backapp = APIRouter()

class RequestClass(BaseModel):
    duration: int
    theme: str
    accommodation_type: str
    budget: str


@backapp.post("/onboarding")
def create_new_user(username: str = Form(), password: str = Form(), email: str = Form()):
    hashed_pw = security.get_pw_hash(password)
    data_handling.create_user(username, hashed_pw, email)
    return RedirectResponse(url="/login")


@backapp.post("/user_page/make_request")
def create_new_request(duration: int = Form(), theme: str = Form(), accommodation: str = Form(), budget: str = Form(), current_user: security.User = Depends(security.get_current_user)):
    request_id = data_handling.store_request(duration, theme, accommodation, budget, current_user.user_id)
    ai_response =  asyncio.run(openai_communication.send_gpt_request(RequestClass(duration=duration, theme=theme, accommodation_type=accommodation, budget=budget)))
    data_handling.store_response(ai_response, request_id)
    return ai_response


@backapp.delete("/user_page/delete_response")
def delete_response(response_id: int = Form(default="REQUEST_ID"), current_user: security.User = Depends(security.get_current_user)):
    data_handling.delete_response(response_id, current_user.user_id)
    return "response deleted"


@backapp.put("/user_page/update_request")
def change_request(id: int = Form(), duration: int = Form(default=0), theme: str = Form(default=""), accommodation: str = Form(default=""), budget: str = Form(default=""), current_user: security.User = Depends(security.get_current_user)):
    data_handling.update_request(id, duration, theme, accommodation, budget)
    return "done"


@backapp.delete("/user_page/delete_request")
def delete_request(id: int =Form(), current_user: security.User = Depends(security.get_current_user)):
    return data_handling.delete_request_by_id(id, current_user)


@backapp.put("/user_page/update_user")
def update_user(current_user: security.User = Depends(security.get_current_user), username: str = Form(default=""), old_password: str = Form(default=""),new_password: str = Form(default=""), email: str = Form(default="")):
    return data_handling.update_user(current_user, username, old_password, new_password, email)


@backapp.delete("/user_page/delete_user")
def delete_user(current_user: security.User = Depends(security.get_current_user), password: str = Form(default="")):
    return data_handling.delete_user(current_user, password)