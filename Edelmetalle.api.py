import requests

def get_metal_prices(api_key):
    """Funktion zum Abrufen von aktuellen Edelmetallpreisen und Währungsumrechnungsraten."""
    url = f"https://api.metalpriceapi.com/v1/latest?api_key={api_key}&base=USD&symbols=XPD,XAG,XIR,UAH,EUR"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Überprüfung auf HTTP-Fehler
        
        data = response.json()
        return {
            "palladium_price": data['rates']['UAH'],
            "silver_price": data['rates']['EUR'],
            "iridium_price": data['rates']['EUR'],
            "uah_rate": data['rates']['UAH'],
            "eur_rate": data['rates']['EUR']
        }
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None

def print_metal_prices(metal_prices):
    """Funktion zum Drucken der abgerufenen Edelmetallpreise und Währungsumrechnungsraten."""
    border = "+" + "-" * 48 + "+"
    header = f"| Current Metal Prices and Currency Exchange Rates"
    palladium = f"| Palladium Price: {metal_prices['palladium_price']} USD/oz {' ' * 15}"
    silver = f"| Silver Price: {metal_prices['silver_price']} USD/oz {' ' * 18}"
    iridium = f"| Iridium Price: {metal_prices['iridium_price']} USD/oz {' ' * 17}"
    uah = f"| 1 USD = {metal_prices['uah_rate']} UAH {' ' * 24}"
    eur = f"| 1 USD = {metal_prices['eur_rate']} EUR {' ' * 24}"

    print(border)
    print(header)
    print(border)
    print(palladium)
    print(silver)
    print(iridium)
    print(uah)
    print(eur)
    print(border)

def main():
    """Hauptfunktion des Programms."""
    api_key = "697d45a564bef287e6c7532ca31cbd9e"  # Dein API-Schlüssel hier einfügen

    metal_prices = get_metal_prices(api_key)
    if metal_prices:
        print_metal_prices(metal_prices)
    else:
        print("Fehler beim Abrufen der Edelmetallpreise und Währungsumrechnungsraten.")

if __name__ == "__main__":
    main()
