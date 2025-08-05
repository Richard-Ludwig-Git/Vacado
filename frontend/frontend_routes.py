from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from backend import data_handling, security



routing = APIRouter()
page = Jinja2Templates(directory="frontend")


@routing.get("/")
def root(req: Request):
    return page.TemplateResponse(
        name="root.html",
        context={"request": req})


@routing.get("/vacation_request_page")
def make_vacation_choise(req: Request, current_user: security.User = Depends(security.get_current_user)):
    return page.TemplateResponse(
        name="make_vacation.html",
        context={"request": req, "username": current_user.user_name})


@routing.get("/onboarding_page")
def register(req: Request):
    return page.TemplateResponse(
        name="onboarding.html",
        context={"request": req})


@routing.get("/login_page")
def login(req: Request):
    return page.TemplateResponse(
        name="login.html",
        context={"request": req})


@routing.get("/user_page")
def show_user_profile_page(request: Request, current_user: security.User = Depends(security.get_current_user)):
    return page.TemplateResponse("user-template.html", {
        "request": request,
        "username": current_user.user_name,
        "useremail": current_user.email,
        "userrequests": data_handling.get_requests_by_userid(current_user.user_id)
    })