from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class WeatherRequest(BaseModel):
    city: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API"}

@app.post("/weather")
def get_weather(request: WeatherRequest):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": request.city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found")
    data = response.json()
    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    return weather_data
