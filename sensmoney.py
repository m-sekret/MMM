import requests
import time
import random

def get_random_currency_rates():
    rates = {
        'usd_uah': round(random.uniform(26, 30), 2),
        'usd_eur': round(random.uniform(0.8, 1.2), 3),
        'usd_gbp': round(random.uniform(0.7, 1.0), 3)
    }
    return rates

while True:
    try:
        data = get_random_currency_rates()
        response = requests.post('http://localhost:5000/update', json=data)
        print(f"Sent data: {data}, Response: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(300)  # Update every 5 minutes
