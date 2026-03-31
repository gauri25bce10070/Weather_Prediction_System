# WEATHER PREDICTION SYSTEM

# Overview
This project focuses on predicting whether it will rain or not using a Machine Learning approach. It analyzes key weather parameters such as temperature, humidity, atmospheric pressure, and wind speed to classify the weather condition.
The system is designed to work with both real-time weather data (via API) and manually provided inputs, ensuring flexibility and reliability.

# Objective of this project
The primary objective of this project is to develop a predictive model that can accurately determine the likelihood of rainfall based on environmental conditions. This helps in understanding how machine learning can be applied to real-world problems like weather forecasting.

# Features of this project
- Rain Prediction using Machine Learning
- Uses Important Weather Parameters
- Real-Time Data Integration (API Support)
- Machine Learning Model (Random Forest)

# Methodology of this project
The project follows a structured machine learning workflow:

- A dataset containing weather attributes is used to train the model
- Relevant features (temperature, humidity, pressure, wind speed) are selected
- A classification algorithm (Random Forest) is applied
- The model learns patterns and relationships within the data
- Based on new input data, the model predicts whether it will rain or not

# Technologies Used
- Python – for implementation
- NumPy – for numerical computations
- Scikit-learn – for machine learning model
- Requests – for fetching real-time data from API

# API Integration
The project supports integration with the OpenWeather API to obtain real-time weather information. This enhances the practicality of the model by allowing predictions based on live data.
Note: API usage is optional, and the system can function using manual inputs if the API is unavailable.

# Features Considered
The prediction model is based on the following weather parameters:
- Temperature (°C)
- Humidity (%)
- Atmospheric Pressure (hPa)
- Wind Speed

# Execution Steps
- Install Required Libraries
pip install numpy scikit-learn requests
- Run the Program
python rain_prediction.py
- Provide Input
Either automatic (via API)
Or manual input (user-defined values)

# Sample Output
Weather Data: [30, 70, 1012, 5]
Prediction: Rain Expected 

# Future Scope
This project can be further enhanced by:
- Using a larger and more diverse dataset for improved accuracy
- Implementing advanced models such as Neural Networks
- Developing a graphical user interface (GUI)
- Deploying the system as a web or mobile application
- Integrating more weather parameters for better prediction

# Conclusion

This project demonstrates the practical application of machine learning in weather prediction. It highlights how data-driven models can be used to make informed predictions and solve real-world problems efficiently.

# Output

<img width="1418" height="180" alt="image" src="https://github.com/user-attachments/assets/f2ba5e35-b976-4038-9979-18f07039b332" />
