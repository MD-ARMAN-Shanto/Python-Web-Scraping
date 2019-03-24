import urllib
import urllib.request
from bs4 import BeautifulSoup

my_url = 'http://books.toscrape.com/'

page = urllib.request.urlopen(my_url)
soup = BeautifulSoup(page, 'html.parser')

#print(soup.findAll('div'))

"""file_name = "book_store.csv"
f = open(file_name, "w")
header = 'book_name, price, cart, stock'
f.write(header+ '\n')"""

for content in soup.findAll('ol', {'class': 'row'}):
    for result in content.findAll('li',{'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}):
        for price in result.findAll('div', {'class': 'product_price'}):
            print1 = (result.find('h3').text)
            print2 = (price.find('p').text)
            print3 = ( price.find("form").text)
            #print4 = (price.find('form').text)
            #hola = print3+print4
            hello = print1+ " " +  print2+ print3 +'in stock'


            print(hello)

