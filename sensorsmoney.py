import requests
import time

url = 'http://localhost:5000/update'
api_url = 'https://api.exchangerate-api.com/v4/latest/USD'

while True:
    response = requests.get(api_url)
    data = response.json()
    sensors_data = {
        "hryvnia_dollar": data['rates']['UAH'],
        "dollar_euro": data['rates']['EUR'],
        "dollar_pound": data['rates']['GBP']
    }
    post_response = requests.post(url, json=sensors_data)
    print(f"Sent data: {sensors_data}, Response: {post_response.status_code}")
    time.sleep(300)  # Оновлення  кажні 5 хв
