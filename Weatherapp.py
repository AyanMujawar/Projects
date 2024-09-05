import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

city= input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

if weather_data.status_code== 404:
    print("No City Found")
else:
    # print(weather_data.json())
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is: {weather}")
    print(f"The temperature in {city} is: {temp} °C")

