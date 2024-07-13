import time
import random
import requests

companies = ["IBM", "bayractar", "cisco"]

def generate_price():
    return round(random.uniform(100, 500), 2)

while True:
    data = {company: generate_price() for company in companies}
    try:
        response = requests.post('http://localhost:5000/update', json=data)
        print("Data sent:", data)
        print("Server response:", response.json())
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(5)
