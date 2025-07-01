import json
import requests
from bs4 import BeautifulSoup
import time

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

headers = {
    "User-Agent": "Mozilla/5.0"
}

def search_coupang_link(query):
    url = f"https://www.coupang.com/np/search?q={requests.utils.quote(query)}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    link_tag = soup.select_one("a.search-product-link")
    if link_tag:
        return "https://www.coupang.com" + link_tag["href"].split('?')[0]
    return ""

for product in products:
    query = product["name"]
    link = search_coupang_link(query)
    product["link"] = link
    time.sleep(1.5)

with open("products_with_links.json", "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)
