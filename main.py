import requests
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = np.array([
    [30, 70, 1012, 5],
    [35, 40, 1015, 3],
    [28, 80, 1008, 6],
    [33, 50, 1013, 2],
    [25, 90, 1005, 7]
])
y = np.array([1, 0, 1, 0, 1])

model = RandomForestClassifier()
model.fit(X, y)

API_KEY = "cb4af9bf1808270eca31484e8a6963ec" 
CITY = "Jaipur"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    print("API Response:", data)

    if "main" not in data:
        print(" API Error:", data.get("message", "Unknown error"))
        return None

    return [
        data["main"]["temp"],
        data["main"]["humidity"],
        data["main"]["pressure"],
        data["wind"]["speed"]
    ]

def predict_rain(weather):99999999996
    input_data = np.array(weather).reshape(1, -1)
    prediction = model.predict(input_data)
    return " Rain Expected" if prediction[0] == 1 else " No Rain"

weather = get_weather()

if weather:
    result = predict_rain(weather)
    print("Weather Data:", weather)
    print("Prediction:", result)
else:
    print(" Could not fetch weather data")
