#import yfinance as yf
#import pandas as pd
#import matplotlib.pyplot as plt
from datetime import datetime
import time
import random
import requests

#def get_stock_data(tickers):
    # Завантажуємо дані для кожного з тикерів
 #   data = yf.download(tickers, period='1d', interval='1m')
  #  return data['Adj Close']

#def plot_data(closing_prices):
 #   closing_prices.plot(figsize=(14, 7))
  #  plt.title('Ціни акцій Intel, AMD та Nvidia')
   # plt.xlabel('Дата')
#    plt.ylabel('Ціна (USD)')
 #   plt.legend(closing_prices.columns)
  #  plt.show()

url = 'http://localhost:5000/update'
tickers = ['Intel', 'AMD', 'Nvidia']

def generate_tickers():
    data = {
        'Intel' : round(random.uniform(100, 200), 2),
        'AMD' : round(random.uniform(100, 200), 2),
        'Nvidia' : round(random.uniform(100, 200), 2),
    }
    return data

while True:
    tickers = generate_tickers()
    print(f"Оновлення даних: {datetime.now()}: {tickers}")
    response = requests.post(url, json=tickers)
   # print(closing_prices.tail())

    # Візуалізуємо дані
 #   plot_data(closing_prices)

    # Зберігаємо дані в CSV-файл
  #  closing_prices.to_csv('stock_prices.csv')

    # Очікуємо 5 хвилин перед наступним оновленням
    time.sleep(300)
