from selenium import webdriver
import ebay
import amazon
def write_to_csv(filename, list_products):
    f = open(filename, "a")
    f.write("NameWeabsite,NameProduct,Price,Link\n")
    for product in list_products:
        nameWebsite = product[0]
        name = product[1]
        price = product[2]
        link = product[3]
        f.write("{},{},{},{}\n".format(nameWebsite, name.encode("utf-8"), price.encode("utf-8"), link.encode("utf-8")))
    f.close()
def parsePrice(price):
    return float(price.split(" to ")[0][1:])

def combine ():
    products = []
    f1 = open("listproductsEbay.csv", "r")
    f2 = open("listproductsAmazon.csv", "r")
    for i in f1.readlines():
        product =  i.split(",")
        if(not i[1] in["Name", "Price", "Link"]):
            products.append(product)
    for i in f2.readlines():
        product =  i.split(",")
        if(not i[1] in["Name", "Price", "Link"]):
            products.append(product)
    
    for i in range(len(products)-1):
        for j in range(i+1, len(products)-1):
            if parsePrice(products[i][2]) > parsePrice(products[j][2]):
                tmp = products[i]
                products[i] = products[j]
                products[j] = tmp           
    write_to_csv("sortproducts.csv", products)
    for i in products:
        print (parsePrice(i[2]))

combine()
