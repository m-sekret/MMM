import requests
import random
import time

url = 'http://localhost:5000/update'

prices = {
    "Mercury": 525.00,
    "Palladium": 2250.00,
    "Copper": 4.50
}

def update_price(price, volatility):
    """Simulates price update with some volatility."""
    change_percent = random.uniform(-volatility, volatility)
    new_price = price * (1 + change_percent / 100)
    return round(new_price, 2)

def simulate_market():
    """Simulates market behavior."""
    global prices
    prices["Mercury"] = update_price(prices["Mercury"], 2)
    prices["Palladium"] = update_price(prices["Palladium"], 1)
    prices["Copper"] = update_price(prices["Copper"], 0.5)
    return prices

while True:
    precious_metals = simulate_market()

    response = requests.post(url, json=precious_metals)
    print(f"Sent data: {precious_metals}, Response: {response.status_code}")

    time.sleep(random.randint(20, 40))
