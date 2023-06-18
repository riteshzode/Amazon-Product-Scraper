import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd


def get_data(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.ie}
    with requests.Session() as session:
        r = session.get(url, headers=headers)
        r.raise_for_status()
        return r.text


def get_single_product_detail(url):
    soup = BeautifulSoup(get_data(url), 'html.parser')

    title = soup.find(id="title", class_="a-size-large").text.strip()
    price = soup.find(class_="a-price-whole").text.replace(".", "").replace(",", "")
    rating = soup.find(class_="a-icon-alt").text

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}\n")

    return title, price, rating


def scrape_products(url):
    soup = BeautifulSoup(get_data(url), 'html.parser')

    product_urls = set()
    for link in soup.find_all("a"):
        try:
            url = link.get("href")
            if "/dp/" in url:
                product_urls.add(url)
        except:
            pass

    print(f"Total products found: {len(product_urls)}")

    for url in product_urls:
        if "amazon" not in url:
            try:
                full_url = f"https://www.amazon.in{url}"
                title, price, rating = get_single_product_detail(full_url)

                all_data["Title"].append(title)
                all_data["Price"].append(price)
                all_data["Url"].append(full_url)
                all_data["Rating"].append(rating)

            except Exception as e:
                print(f"An error occurred while scraping a product: {str(e)}")
                pass

    write_to_csv()


def write_to_csv():
    df = pd.DataFrame(all_data)
    df.to_csv("products.csv", index=False)
    print("File created successfully: products.csv")


all_data = {
    "Title": [],
    "Url": [],
    "Price": [],
    "Rating": []
}

if __name__ == "__main__":
    product_name = "monitor" # we can enter any product of our choice
    scrape_products(f"https://www.amazon.in/s?k={product_name}")
