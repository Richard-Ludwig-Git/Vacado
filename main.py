from fastapi import FastAPI, Form
from backend import security, backend_endpoints
from frontend import frontend_routes


vacado = FastAPI()
vacado.include_router(router=security.security_router)
vacado.include_router(router=frontend_routes.routing)
vacado.include_router(router=backend_endpoints.backapp)




"""GPT prompt
You are a smart travel planner assistant. Based on the following user preferences, generate a personalized vacation plan 
    including flights, accommodation, and daily activities. Keep the tone helpful and inspiring.
    Trip Duration: {DURATION} days
    Trip Theme: {THEME}
    Accommodation Type: {ACCOMMODATION_TYPE}
    Budget Level: {BUDGET}
Please include:
    A suggested destination or two that match the theme
    Flight overview (example or average, not real-time data)
    Type of accommodation with a brief description
    Daily itinerary with 1–2 activities per day, fitting the theme and budget
    Optional local tips or food recommendations
Format the output in clear sections with emojis if appropriate. Keep it concise, friendly, and tailored."""

"""GPT response test"""
#response = gptclient.chat.completions.create(
#        model="gpt-4.1",
#    messages=ChatCompletionUserMessageParam[{"role": "user", "content": """Who is Gandalf"""}])



