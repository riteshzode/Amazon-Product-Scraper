# Amazon-Product-Scraper
Amazon Product Scraper" is a Python project that scrapes product details (title, url, price, and rating) from Amazon for a given product search and saves the data in a CSV file

## Setup
1 Clone the project repository.

2 Install the required dependencies by running the following command:

`pip install -r requirements.txt`

3 To run the script, execute the following command:

`python main.py`

## Customization
You can customize the script by modifying the product_name variable in the if __name__ == "__main__" block. This variable determines the product to be searched on Amazon.in. You can change it to any product of your choice.

## Output
The script saves the scraped data to a CSV file named products.csv. The file will be created in the same directory where the script is located. Each row in the CSV file represents a product and contains columns for title, URL, price, and rating.

Note: Please be aware of the legal and ethical implications of web scraping and ensure that you comply with the terms of service of the website you are scraping.
