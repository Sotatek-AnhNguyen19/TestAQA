from selenium import webdriver

driver = webdriver. Chrome(executable_path="D:\Selenium\chromedriver.exe")
driver.get("https://www.ebay.com/")
search = driver.find_element_by_xpath("//input[@id='gh-ac']").send_keys("iPhone 11")
search_button = driver.find_element_by_xpath("//input[@id='gh-btn']"). click()

def write_to_csv(filename, list_products, nameWebsite):
    f = open(filename, "a")
    f.write("NameWeabsite,NameProduct,Price,Link\n")
    for product in list_products:
        name, price, link = product
        f.write("{},{},{},{}\n".format(nameWebsite, name.encode("utf-8"), price.encode("utf-8"), link.encode("utf-8")))
    f.close()
    
list_products = []
results = driver.find_element_by_xpath("//h1[@class='srp-controls__count-heading']/span[1]").text
results = results.replace(',', '')
pages= int(int(results)/50)+1
for i in range(pages):
    products = driver.find_elements_by_xpath("//*[@id='srp-river-results']/ul/li")
    for i in products:
        name = i.find_element_by_class_name("s-item__title").text
        
        price = i.find_element_by_class_name("s-item__price").text
        
        link = i.find_element_by_class_name("s-item__link").get_attribute('href')
        
        product = (name, price, link)
        list_products.append(product)
    button_next = driver.find_element_by_xpath("//a[@aria-label='Go to next search page']")
    button_next.click()
    write_to_csv("listproductsEbay.csv", list_products, "Ebay.com")
    list_products = []

driver.close()
