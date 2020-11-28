from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

options=Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
driver=webdriver.Chrome(options=options)
driver.get("https://www.amazon.com/")
ele=driver.find_element_by_xpath("//a[@aria-label='Computers & Accessories']")
ele.click()
ele=driver.find_element_by_id("twotabsearchtextbox")
ele.send_keys("Samsung SSD")
ele.send_keys(Keys.RETURN)
source=driver.page_source
soup=BeautifulSoup(source,'lxml')
product_list_div=soup.find_all("div",class_="a-section a-spacing-none")
for a_product_div in product_list_div:
	product_title_tag=a_product_div.find_all("span",class_="a-size-medium a-color-base a-text-normal")
	product_link=a_product_div.find_all("a",class_="a-link-normal a-text-normal")
	product_title=""
	for i in product_title_tag:
		product_title=i.string
	if(product_title!=""):
		print(product_title)
		for i in product_link:
			print("Link Product: https://www.amazon.com"+i['href'])
		print("---------------------------------------------------------------")