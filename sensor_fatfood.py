import requests
import random
import time

url = 'http://localhost:5000/update'

while True:
    food_shares = {
        "Cocacola": round(random.uniform(55, 70), 2),
        "Pepsi": round(random.uniform(155, 167), 2),
        "McDonalds": round(random.uniform(243, 261), 2)
    }

    response = requests.post(url, json=food_shares)
    print(f"Sent data: {food_shares}, Response: {response.status_code}")
    time.sleep(30)
