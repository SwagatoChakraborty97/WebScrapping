# Scraping Real Websites - II
# AIM - To Extract the BookName, BookPrice, BookLink from all the webpages of the website
import requests
from bs4 import BeautifulSoup

# response = requests.get("https://books.toscrape.com/")
# print(response.status_code)
# data = BeautifulSoup(response.text, 'html.parser')
# print()
# print(data.prettify())
# print()
# print(data.title)
# print()
# print(data.findAll(text = "Books to Scrape"))
# print(data.get_text(strip=True))

my_urls = []
i = 1
while True:
    response = requests.get(
        f"https://books.toscrape.com/catalogue/page-{i}.html")
    if response.status_code == 200:
        print(f"https://books.toscrape.com/catalogue/page-{i}.html")
        my_urls.append(f"https://books.toscrape.com/catalogue/page-{i}.html")
        i += 1
    else:
        break
print("Appending in a List")
print(len(my_urls))
print(my_urls)
print('Completed Appending Urls to list')

i = 0
for webpage in my_urls:
    response = requests.get(webpage)
    data = BeautifulSoup(response.text, 'html.parser')
    my_list = data.find_all(class_="product_pod")
    for item in my_list:
        BookDetails = []
        BookName = item.h3.string
        BookPrice = item.find(class_="price_color")
        BookLink = "https://books.toscrape.com//catalogue/" + item.h3.a['href']
        # print(BookName)
        # print(f"Price - {BookPrice.string}")
        # print(BookLink)
        # print("-------------------x------------------")
        BookDetails.append(BookName) 
        BookDetails.append(BookPrice.string) 
        BookDetails.append(BookLink) 
        # To Save Data in .csv file 
        # Step - 1 - Create a DataFrame 
        print(BookDetails)
        import pandas as pd
        if i == 0:
            df = pd.DataFrame([BookDetails], columns = ['BookName', 'Current Price', 'Link'])
        else:
            df.loc[i] = BookDetails
        i += 1

# Step - II - Use to_csv() to save
print(df)
df.to_csv("Record of Books.csv")
print("Saved to .csv file")
