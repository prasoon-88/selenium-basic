from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://www.amazon.com/s?k=laptop')

time.sleep(5)


cards = chrome.find_elements(By.CSS_SELECTOR,'.s-result-item')

def getMeta(card):
    try:
        title = card.find_element(By.CSS_SELECTOR,'h2')
        price = card.find_element(By.CSS_SELECTOR,'.a-price-whole')
        # link = card.finf_element(By.CSS_SELECTOR,'a','.a-link-normal .s-line-clamp-2 .s-link-style .a-text-normal')
        return {
            "title":title.text,
            "price":price.text,
            # "link":link.text
        }
    except:
        return 

final = []
if cards:
    for card in cards:
        product = (getMeta(card))
        if(product):
            final.append(product)

for product in final:
    print('Product Name: ',product.get('title',''))
    print('Product price: ', product.get('price',''))
    print('------------------------------------------------')