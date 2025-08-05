from contextlib import nullcontext
from fastapi import APIRouter, Form
from backend import data_handling, security
from fastapi.responses import RedirectResponse
from fastapi.params import Depends


backapp = APIRouter()


@backapp.post("/user_page/make_request")
def create_new_request(duration: int = Form(), theme: str = Form(), accommodation: str = Form(), budget: str = Form(), current_user: security.User = Depends(security.get_current_user)):
    data_handling.store_request(duration, theme, accommodation, budget, current_user.user_id)
    return "done"


@backapp.get("/request")
def get_request(user_id: int = None, request_id: int = None):
    if request_id:
        return data_handling.get_requests_by_id(request_id)
    if user_id:
        return data_handling.get_requests_by_userid(user_id)
    return None


@backapp.put("/user_page/request")
def change_request(id: int = Form(), duration: int = Form(), theme: str = Form(default=""), accommodation: str = Form(default=""), budget: str = Form(default=""), current_user: security.User = Depends(security.get_current_user)):
    data_handling.update_request(id, duration, theme, accommodation, budget)
    return "done"


@backapp.delete("/user_page/request")
def delete_request(id: int =Form(), current_user: security.User = Depends(security.get_current_user)):
    return data_handling.delete_request_by_id(id, current_user)


@backapp.post("/onboarding")
def create_new_user(username: str = Form(), password: str = Form(), email: str = Form()):
    hashed_pw = security.get_pw_hash(password)
    data_handling.create_user(username, hashed_pw, email)
    return RedirectResponse(url="/login")


@backapp.put("/user_page/update")
def update_user(current_user: security.User = Depends(security.get_current_user), username: str = Form(default=""), old_password: str = Form(default=""),new_password: str = Form(default=""), email: str = Form(default="")):
    return data_handling.update_user(current_user, username, old_password, new_password, email)


@backapp.delete("/user_page/delete_user")
def delete_user(current_user: security.User = Depends(security.get_current_user), password: str = Form(default="")):
    return data_handling.delete_user(current_user, password)