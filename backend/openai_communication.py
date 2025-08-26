import asyncio

from openai import AsyncOpenAI
from pydantic import BaseModel
from os import getenv
from dotenv import load_dotenv
import json
from backend import backend_endpoints


load_dotenv("../env/.env")
client = AsyncOpenAI(api_key=getenv('OPENAI_API_KEY'), timeout=120)


class HolidayKeyFacts(BaseModel):
    destination: str
    flights: str
    accommodation_type: str
    activities: str
    food_rec: str


async def send_gpt_request(request):
    response = await client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {"role": "user", "content": f"""You are a smart travel planner assistant. Based on the following user preferences, generate a personalized vacation plan 
                    including flights, accommodation, and daily activities. Keep the tone helpful and inspiring.
                    Trip Duration: {request.duration} days
                    Trip Theme: {request.theme}
                    Accommodation Type: {request.accommodation_type}
                    Budget Level: {request.budget}
                Please include:
                A suggested destination that match the theme
                Flight overview (example or average, not real-time data)
                Type of accommodation with a brief description
                Daily itinerary with 1–2 activities per day, fitting the theme and budget
                Optional local food recommendations
                Format the output in clear sections. Keep it concise, friendly, and tailored. Avoid apostrophe"""}],
                text_format=HolidayKeyFacts,
                store=False,
    )
    json_response = json.loads(response.output_text)
    class_response = HolidayKeyFacts(destination=json_response["destination"], flights=json_response["flights"], accommodation_type=json_response["accommodation_type"], activities=json_response["activities"], food_rec=json_response["food_rec"])
    return class_response



"""testresponse = send_gpt_request(ReqquestClass(duration=2, accommodation_type="hotel", theme="city", budget="low"))"""



