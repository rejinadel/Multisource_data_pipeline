import requests
from bs4 import BeautifulSoup
import pandas as pd
def scrape_data(page):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print(f"failed to connect:{response.status_code}")


    soup = BeautifulSoup(response.text,"html.parser")

    products = soup.find_all("article", class_ = "product_pod")
    extracted_data = []

    for product in products:

        title = product.h3.a["title"]

        price = product.find("p", class_ = "price_color").text
        price = float(price.replace("£",""))
        

        rating_tag = product.find("p", class_ = "star-rating")

        if rating_tag:
            rating = rating_tag["class"][1]
        else:
            rating = None
        
        

        stock = product.find("p", class_ = "instock availability").text.strip()


        extracted_data.append({
            "title":title,
            "price":price,
            "rating":rating,
            "stock":stock
        })
    return extracted_data









