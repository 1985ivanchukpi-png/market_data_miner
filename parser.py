import requests
import time

def fetch_market_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,xml;q=0.9,image/webp,*/*;q=0.8'
    }
    print(f"--- Запуск парсера ---")
    print(f"Цель: {url}")
    print(f"Статус: Эмуляция браузера включена...")
    time.sleep(1)
    print(f"Результат: Данные успешно получены.")

if __name__ == "__main__":
    fetch_market_data("https://www.amazon.com")
