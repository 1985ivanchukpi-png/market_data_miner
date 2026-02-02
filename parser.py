import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def parse_and_export(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    print(f"--- Аналіз сторінки: {url} ---")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        
        for title in soup.find_all(['h1', 'h2', 'h3']):
            name = title.get_text(strip=True)
            if name and len(name) > 5:
                products.append({"Назва товару/Заголовок": name})
        
        # 1. Зберігаємо в JSON (для розробників)
        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, ensure_ascii=False, indent=4)
            
        # 2. Зберігаємо в Excel (для замовників)
        df = pd.DataFrame(products)
        df.to_excel('market_report.xlsx', index=False)
            
        print(f"[Успіх] Зібрано одиниць: {len(products)}")
        print("[Файли] Створено results.json та market_report.xlsx")
        
    except Exception as e:
        print(f"[Помилка]: {e}")

if __name__ == "__main__":
    parse_and_export("https://en.wikipedia.org/wiki/Main_Page")
