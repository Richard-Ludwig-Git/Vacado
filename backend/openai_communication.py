from openai import AsyncOpenAI
from pydantic import BaseModel
from os import getenv
from dotenv import load_dotenv
import json


load_dotenv("../env/.env")
client = AsyncOpenAI(api_key=getenv('OPENAI_API_KEY'), timeout=120)


class HolidayKeyFacts(BaseModel):
    destination: str
    transportation_type: str
    travel_time: str
    accommodation_type: str
    activities: str
    food_rec: str


async def send_gpt_request(request):
    """openai prompt and response"""
    response = await client.responses.parse(
        model="gpt-4.1",
        input=[
            {"role": "user", "content": f"""You are a smart travel planner assistant. Based on the following user preferences, generate a personalized vacation plan 
                    including desired transportation, travel time, accommodation, and daily activities. beware of any special needs. Keep the tone helpful and inspiring.
                    Trip Duration: {request.duration} days
                    Origin City: {request.origin_city}
                    Maximum travel time from Origin: {request.max_travel_time}
                    Desired transportation Type: {request.transportation_type}                    
                    Trip Theme: {request.theme}
                    Accommodation Type: {request.accommodation_type}
                    Budget: {request.budget}
                    Special Need: {request.special_need}
                Please include:
                A suggested destination that match the theme
                Flight overview (example or average, not real-time data)
                Type of accommodation with a brief description
                Daily itinerary with 1–2 activities per day, fitting the theme and budget
                Optional local food recommendations
                Format the output in clear sections. Keep it concise, friendly, and tailored. 
                Dont use any apostrophe"""}],
                text_format=HolidayKeyFacts,
                store=False)
    json_response = json.loads(response.output_text)
    class_response = HolidayKeyFacts(destination=json_response["destination"], transportation_type=json_response["transportation_type"], travel_time=json_response["travel_time"], accommodation_type=json_response["accommodation_type"], activities=json_response["activities"], food_rec=json_response["food_rec"])
    return class_response




