# API de Previsão do Tempo com FastAPI

<aside>
Esta é uma API simples para consultar informações meteorológicas usando FastAPI e OpenWeatherMap.

</aside>

## Requisitos Iniciais

- Python
- Conta no OpenWeatherMap
- Conhecimento básico de Python e APIs

## Estrutura do Projeto

```
weather_api/
├── main.py         # Arquivo principal da API
├── .env           # Variáveis de ambiente
├── requirements.txt # Dependências
└── test_request.py # Script de teste
```

## Guia de Instalação

### 1. Configuração do Ambiente

- Instale o Python: [python.org](https://www.python.org/downloads/)
- Configure o Ambiente Virtual:
    
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Linux/MacOS
    ```
    
- Instale as Dependências:
    
    ```
    # requirements.txt
    fastapi
    uvicorn
    requests
    python-dotenv
    pydantic
    ```
    

Execute: `pip install -r requirements.txt`

### 2. Configuração da API OpenWeatherMap

- Crie uma conta em [OpenWeatherMap](https://openweathermap.org/api)
- Obtenha sua chave API no painel
- Configure o arquivo .env:
    
    ```
    OPENWEATHER_API_KEY=sua_chave_aqui
    ```
    

### 3. Desenvolvimento e Execução

- Inicie o servidor: `uvicorn main:app --reload`
- Acesse a documentação: `http://127.0.0.1:8000/docs`
- Teste a API executando o script test_request.py

5. Atualizações Futuras
Desenvolver uma interface web para buscar informações meteorológicas especificas utilizando Next.js.

### 4. Links Úteis

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [Documentação OpenWeatherMap](https://openweathermap.org/api)
- [Documentação Heroku](https://devcenter.heroku.com/)

### 5. Codigos template

**main.py**

```python
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

```

**test_request.py**

```python
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
```
