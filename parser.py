import requests
from bs4 import BeautifulSoup
import json

def parse_demo_market(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print(f"--- Подключение к: {url} ---")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        # Ищем все заголовки h2 (часто используются для названий товаров)
        for title in soup.find_all('h2'):
            name = title.get_text(strip=True)
            if name:
                products.append({"product_name": name})
        
        # Сохраняем результат в JSON
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
            
        print(f"[Успех] Найдено товаров: {len(products)}")
        print("[Инфо] Данные сохранены в results.json")
        
    except Exception as e:
        print(f"[Ошибка] Не удалось спарсить данные: {e}")

if __name__ == "__main__":
    # Используем проверенный сайт для теста (например, Wikipedia или демо-магазин)
    parse_demo_market("https://en.wikipedia.org/wiki/Main_Page")
