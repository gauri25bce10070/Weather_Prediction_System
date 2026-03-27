import requests
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# TRAIN MODEL
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

API_KEY = "YOUR_API_KEY"
CITY = "Jaipur"

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    # PRINT FOR DEBUG
    print("API Response:", data)

    # HANDLE ERROR
    if "main" not in data:
        print(" API Error:", data.get("message", "Unknown error"))
        return None

    return [
        data["main"]["temp"],
        data["main"]["humidity"],
        data["main"]["pressure"],
        data["wind"]["speed"]
    ]

def predict_rain(weather):
    prediction = model.predict([weather])
    return " Rain Expected" if prediction[0] == 1 else " No Rain"

# RUN
weather = get_weather()

if weather:
    result = predict_rain(weather)
    print("Weather Data:", weather)
    print("Prediction:", result)
else:
    print(" Could not fetch weather data")
