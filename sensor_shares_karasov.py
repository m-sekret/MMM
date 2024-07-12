import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time

def get_stock_data(tickers):
    # Завантажуємо дані для кожного з тикерів
    data = yf.download(tickers, period='1d', interval='1m')
    return data['Adj Close']

def plot_data(closing_prices):
    closing_prices.plot(figsize=(14, 7))
    plt.title('Ціни акцій Intel, AMD та Nvidia')
    plt.xlabel('Дата')
    plt.ylabel('Ціна (USD)')
    plt.legend(closing_prices.columns)
    plt.show()

tickers = ['INTC', 'AMD', 'NVDA']

while True:
    print(f"Оновлення даних: {datetime.now()}")
    closing_prices = get_stock_data(tickers)
    print(closing_prices.tail())

    # Візуалізуємо дані
    plot_data(closing_prices)

    # Зберігаємо дані в CSV-файл
    closing_prices.to_csv('stock_prices.csv')

    # Очікуємо 5 хвилин перед наступним оновленням
    time.sleep(300)
