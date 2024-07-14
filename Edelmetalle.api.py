import requests
import random
import time

def get_metal_prices(api_key):
    """Funktion zum Abrufen von aktuellen Edelmetallpreisen und Währungsumrechnungsraten."""
    url = f"https://api.metalpriceapi.com/v1/latest?api_key={api_key}&base=USD&symbols=XPD,XAG,XIR,UAH,EUR"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüfung auf HTTP-Fehler
        
        data = response.json()
        return {
            "paladium_freier": data['rates']['UAH'],
            "silver_freier": data['rates']['EUR'],
            "iridium_freier": data['rates']['EUR'],
        }
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None

url = 'http://localhost:5000/update'
api_key = "697d45a564bef287e6c7532ca31cbd9e" 

while True:
    metal_prices = get_metal_prices(api_key)

    response = requests.post(url, json=metal_prices)
    print(f"Sent data: {metal_prices}, Response: {response.status_code}")
    time.sleep(60)