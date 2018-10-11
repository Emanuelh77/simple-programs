from bs4 import BeautifulSoup
import requests

product_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&N=-1&isNodeId=1"

#opening up connection
res = requests.get(product_url)

#html parsing
page_soup = BeautifulSoup(res.text, 'html.parser')

#takes each product in div
containers = page_soup.findAll("div",{"class": "item-container"})

filename = "graphics_cards.csv"
f = open(filename, "w")

#the commas mean new cell in excel
#added \n because csv are delimited by new line
headers = "brand, product name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]        #finds the text with the tag 'tittle'
    title_container = container.findAll("a",{"class": "item-title"})    #takes everything from within that class
    product_name = title_container[0].text      #takes the text from title_container which is the product name

    shipping_container = container.findAll("li",{"class": "price-ship"})
    #print(len(shipping_container))
    shipping_cost = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product name: " + product_name)
    print("shipping: " + shipping_cost)
    print("\n")

    f.write(brand + "," + product_name.replace(",","|") + "," + shipping_cost + "\n")

f.close()









