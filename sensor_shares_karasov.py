import random
import time

def generate_random_price(symbol):
    return round(random.uniform(100, 500), 2)

def display_stock_prices():
    while True:
        intel_price = generate_random_price('INTC')
        amd_price = generate_random_price('AMD')
        nvidia_price = generate_random_price('NVDA')

        print(f"Intel (INTC): ${intel_price}")
        print(f"AMD (AMD): ${amd_price}")
        print(f"Nvidia (NVDA): ${nvidia_price}")

        time.sleep(5)  # Оновлення кожні 5 секунд

if __name__ == "__main__":
    display_stock_prices()
