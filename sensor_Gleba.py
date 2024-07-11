import requests
import random
import time

def detect_precious_metals():
    metals = ["gold", "platinum", "silver"]
    detected_metal = random.choice(metals)
    return detected_metal

url = 'http://localhost:5000/update'

while True:
    metal = detect_precious_metals()
    metal_data = {"metal": metal}

    try:
        response = requests.post(url, json=metal_data)
        response.raise_for_status()
        print(f"Sent data: {metal_data}, Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

    time.sleep(30)
