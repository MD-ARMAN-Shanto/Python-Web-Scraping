from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.daraz.com.bd/#hp-just-for-you"

uClint = uReq(my_url)
page_html = uClint.read()
uClint.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "hp-card-mod-header"})

file_name = "product.csv"
f = open(file_name, "w")
headers = "brand, shipping"
f.write(headers)

for container in containers:
    brand_container = container.findAll("div", {"class": "title"})
    brand = brand_container[0].text
    #title_container = container.findAll("a", {"class": "item-title"})
    #product_name = title_container.text.strip()
    shipping_container = container.findAll("a", {"class": "ProfileCardMini-avatar profile-picture js-tooltip"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("shipping:" + shipping)

f.write(brand , shipping + "\n")

f.close()