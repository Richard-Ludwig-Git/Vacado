from fastapi import APIRouter, Request
from fastapi.params import Depends
from fastapi.templating import Jinja2Templates
from backend import data_handling, security


routing = APIRouter(tags=["frontend"])
page = Jinja2Templates(directory="frontend")


@routing.get("/")
def root(req: Request):
    """endpoint to lead to landing-page """
    return page.TemplateResponse(
        name="root.html",
        context={"request": req})


@routing.get("/vacation_request_page")
def send_vacation_choice(req: Request, current_user: security.User = Depends(security.get_current_user)):
    """secured endpoint to lead to request-page"""
    return page.TemplateResponse(
        name="make_vacation.html",
        context={"request": req, "username": current_user.user_name})


@routing.get("/login_page")
def login(req: Request):
    """endpoint to lead to login page"""
    return page.TemplateResponse(
        name="login.html",
        context={"request": req})


@routing.get("/user_page")
def show_user_profile_page(request: Request, current_user: security.User = Depends(security.get_current_user)):
    """secure endpoint to lead to user page"""
    return page.TemplateResponse("user-template.html", {
        "request": request,
        "username": current_user.user_name,
        "useremail": current_user.email,
        "userrequests": data_handling.get_requests_by_userid(current_user.user_id)})


@routing.get("/onboarding_page")
def register(req: Request):
    """endpoint to lead to registration page"""
    return page.TemplateResponse(
        name="onboarding.html",
        context={"request": req})




