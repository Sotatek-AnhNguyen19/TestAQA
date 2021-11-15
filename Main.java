package org.sotatek;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class Main {
//    ham combine read va write theo Object nen ko can ham nay
//    public void writeToCsv(String filename, List<String> list_products)
//    {
//        FileWriter myWriters = new FileWriter("D:\\Selenium\\helloworld\\Setel\\combine.csv");
//        myWriters.write("NameWeabsite,NameProduct,Price,Link\n");
//        for (Product product : list_products)
//        {
//            myWriters.write(String.format("{},{},{},{}\n", product.getnameWebsite(), Helper.encodeString(product.getName()), product.getPrice(), Helper.encodeString(product.getLink()));
//        }
//        myWriters.close();
//    }
    public  void parsePrice(String price)
    {
        return float(price.split(" to ")[0][1:])
    }
    public void combine() throws IOException, ClassNotFoundException {
        List<Product> products = new ArrayList<Product>();
        FileInputStream fi = new FileInputStream("listproductsEbay.csv");
        ObjectInputStream ois = new ObjectInputStream(fi);
        Product pr = (Product) ois.readObject();
        ois.close();
        fi.close();
        FileOutputStream fo= new FileOutputStream("combine.csv");
        FileOutputStream oos = new FileOutputStream(fo);
        oos.writeObject(pr);
        oos.close();
        fo.close();

        FileInputStream fi = new FileInputStream("listproductsAmazon.csv");
        ObjectInputStream ois = new ObjectInputStream(fi);
        Product pr = (Product) ois.readObject();
        ois.close();
        fi.close();
        FileOutputStream fo= new FileOutputStream("combine.csv");
        FileOutputStream oos = new FileOutputStream(fo);
        oos.writeObject(pr);
        oos.close();
        fo.close();

        for (int i=0, i< products.size().length()-1, i++){
            for (int j=i+1; j< products.size().length(), j++){
                if (parsePrice(products[i][2]) > parsePrice(products[j][2])){
                    tmp = products[i];
                    products[i] = products[j];
                    products[j] = tmp;
                }
            }
        }

//        writeToCsv("sortproducts.csv", products);
    }

    public static void main (String[] args){
        System.setProperty("webdriver.chrome.driver", "D:\\Selenium\\chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.manage().window().maximize();
        combine();
        driver.quit();

    }
}


