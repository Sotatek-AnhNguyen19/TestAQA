from selenium import webdriver

driver = webdriver. Chrome(executable_path="D:\Selenium\chromedriver.exe")
driver.get("https://www.amazon.com/")
search = driver.find_element_by_id("twotabsearchtextbox").send_keys("iPhone 11")
search_button = driver.find_element_by_id("nav-search-submit-button"). click()
    
def write_to_csv(filename, list_products, nameWebsite):
    f = open(filename, "a")
    f.write("NameWeabsite,NameProduct,Price,Link\n")
    for product in list_products:
        name, price, link = product
        f.write("{},{},{},{}\n".format(nameWebsite, name.encode("utf-8"), price.encode("utf-8"), link.encode("utf-8")))
    f.close()
    
list_products = []
button_next = driver.find_element_by_class_name("a-last")
while (button_next.is_enabled()):
    products = driver.find_element_by_class_name("s-main-slot")
    for i in products:
        name = i.find_element_by_class_name("a-size-base-plus").text
        
        price = i.find_element_by_class_name("a-price-whole").text
        
        link = i.find_element_by_class_name("a-link-normal").get_attribute('href')
        
        product = (name, price, link)
        list_products.append(product)
    button_next = driver.find_element_by_class_name("a-last")
    button_next.click()
    write_to_csv("listproductsAmazon.csv", list_products, "Amazon.com")
    list_products = []

driver.close()
