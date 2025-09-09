from fastapi import APIRouter, Form
from backend import data_handling, security, openai_communication
from fastapi.responses import RedirectResponse
from fastapi.params import Depends
from pydantic import BaseModel
import asyncio


backapp = APIRouter()


class RequestClass(BaseModel):
    duration: int
    origin_city: str
    transportation_type: str
    max_travel_time: int
    theme: str
    accommodation_type: str
    budget: str
    special_need: str


@backapp.post("/onboarding")
def create_new_user(username: str = Form(default=""), password: str = Form(default=""), email: str = Form(default="")):
    """unsecured endpoint to create a new user"""
    hashed_pw = security.get_pw_hash(password)
    data_handling.create_user(username, hashed_pw, email)
    return RedirectResponse(url="/frontend/login")


@backapp.post("/user_page/make_request")
def create_new_request(duration: int = Form(default="Days"),
                       origin_city: str = Form(),
                       transportation_type: str = Form(),
                       max_travel_time: int = Form(default="Hours"),
                       theme: str = Form(),
                       accommodation: str = Form(),
                       budget: str = Form(default="Euro"),
                       special_need: str = Form(default=""),
                       current_user: security.User = Depends(security.get_current_user)):
    """secured endpoint inside user area to make vacation request -- sending openai request, store the request and response"""
    vacation_request = RequestClass(duration=duration, origin_city=origin_city, transportation_type=transportation_type, max_travel_time=max_travel_time, theme=theme, accommodation_type=accommodation, budget=budget, special_need=special_need)
    request_id = data_handling.store_request(vacation_request, current_user.user_id)
    openai_response =  asyncio.run(openai_communication.send_gpt_request(vacation_request))
    data_handling.store_response(openai_response, request_id, current_user.user_id)
    return openai_response

@backapp.get("/user_page/show_vacations")
def get_vacations(current_user: security.User = Depends(security.get_current_user)):
    vacations = {}
    user_requests_data = data_handling.get_requests_by_userid(current_user.user_id)
    for request in user_requests_data:
        response = data_handling.get_response_id_by_request_id(request[0])
        print(response)
        vacations[f"Request {request[0]}"] = {
                                f"Request" : {
                                    "Duration" : f"{request[1]} Days",
                                    "Theme" : request[2],
                                    "Accommodation" : request[3],
                                    "Budget" : f"{request[4]}€",
                                    "Origin" : request[7],
                                    "Transportation" : request[8],
                                    "Special Need" : request[10],},
                                "Result" : {
                                    "Destination" : response[0][1],
                                    "Travel Time" : response[0][8],
                                    "Accommodation" : response[0][3],
                                    "Activities" : response[0][4],
                                    "Food Recommendation" : response[0][5],
                                }
        }
    return vacations


@backapp.delete("/user_page/delete_response")
def delete_response(response_id: int = Form(default="RESPONSE_ID"), current_user: security.User = Depends(security.get_current_user)):
    """secured endpoint inside user area to delete a response from the DB"""
    data_handling.delete_response(response_id, current_user.user_id)
    return "response deleted"


@backapp.put("/user_page/update_request")
def change_request(request_id: int = Form(),
                   duration: int = Form(default=0),
                   origin_city: str = Form(default=""),
                   transportation_type: str = Form(default=""),
                   max_travel_time: int = Form(default=0),
                   theme: str = Form(default=""),
                   accommodation: str = Form(default=""),
                   budget: str = Form(default=""),
                   special_need: str = Form(default=""),
                   current_user: security.User = Depends(security.get_current_user)):
    """secured endpoint inside user area to update a request and get an updated response"""
    updated_request = data_handling.update_request(request_id, duration, origin_city, transportation_type, max_travel_time, theme, accommodation, budget, special_need)
    vacation_request = RequestClass(duration=updated_request[1], origin_city=updated_request[7], transportation_type=updated_request[8],
                                    max_travel_time=updated_request[5], theme=updated_request[2], accommodation_type=updated_request[3],
                                    budget=updated_request[4], special_need=updated_request[10])
    openai_response = asyncio.run(openai_communication.send_gpt_request(vacation_request))
    data_handling.store_response(openai_response, request_id, current_user.user_id)
    return openai_response


@backapp.delete("/user_page/delete_request")
def delete_request(request_id: int =Form(), current_user: security.User = Depends(security.get_current_user)):
    """secured endpoint inside user area to delete a request from the DB"""
    return data_handling.delete_request_by_id(request_id, current_user)


@backapp.put("/user_page/update_user")
def update_user(current_user: security.User = Depends(security.get_current_user), username: str = Form(default=""), old_password: str = Form(default=""),new_password: str = Form(default=""), email: str = Form(default="")):
    """secured endpoint inside user area to update user info"""
    return data_handling.update_user(current_user, username, old_password, new_password, email)


@backapp.delete("/user_page/delete_user")
def delete_user(current_user: security.User = Depends(security.get_current_user), password: str = Form(default="")):
    """secured endpoint inside user area to delete user profile"""
    return data_handling.delete_user(current_user, password)