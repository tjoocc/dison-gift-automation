import json
import requests
from bs4 import BeautifulSoup
import time

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

headers = {
    "User-Agent": "Mozilla/5.0"
}

cache = {}

def search_coupang_link(query):
    if query in cache:
        return cache[query]
    url = f"https://www.coupang.com/np/search?q={requests.utils.quote(query)}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    tag = soup.select_one("a.search-product-link")
    link = "https://www.coupang.com" + tag["href"].split("?")[0] if tag else ""
    cache[query] = link
    time.sleep(0.5)  # 속도 개선: 더 빠르게
    return link

for product in products:
    product["link"] = search_coupang_link(product["name"])

with open("products_with_links.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
