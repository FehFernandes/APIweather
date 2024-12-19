import requests

def test_weather_api():
    # API endpoint
    url = "http://localhost:8000/weather"
    
    # City to search
    data = {"city": "São João Evangelista"}
    
    try:
        # Make POST request
        response = requests.post(url, json=data)
        
        # Check if request was successful
        if response.status_code == 200:
            weather_data = response.json()
            print("Weather Data:")
            print(f"City: {weather_data['city']}")
            print(f"Temperature: {weather_data['temperature']}°C")
            print(f"Description: {weather_data['description']}")
            print(f"Humidity: {weather_data['humidity']}%")
            print(f"Wind Speed: {weather_data['wind_speed']} m/s")
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            
    except requests.exceptions.ConnectionError:
        print("Error: Make sure the FastAPI server is running")

if __name__ == "__main__":
    test_weather_api()