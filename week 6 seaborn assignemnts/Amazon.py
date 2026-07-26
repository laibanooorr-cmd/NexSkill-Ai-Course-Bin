import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

url = "https://www.amazon.com/s?k=mobile+phones"

response = requests.get(url, headers=headers)
print(response.status_code) 

soup = BeautifulSoup(response.text, 'html.parser')

productsList = []
products = soup.find_all('div', {'data-component-type': 's-search-result'})
print(f"Total products found: {len(products)}")

for product in products:
    productDictionary = dict()
    name_tag = product.find('h2')
    productDictionary['Product_Name'] = name_tag.get_text(strip=True) if name_tag else 'NA'
    
    price_tag = product.find('span', class_='a-offscreen')
    productDictionary['Product_Price'] = price_tag.get_text(strip=True) if price_tag else 'NA'
    
    productsList.append(productDictionary)

df = pd.DataFrame(productsList)
print(df)
df.to_csv('Amazon_mobilesphones.csv', index=False, encoding='utf-8')