from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.chrome.service import *
# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
service=Service(executable_path=r"C:\Users\rskch\Desktop\Python\Project 128\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions ()
browser = webdriver.Chrome(service = service,options = options)
browser.get(START_URL)

soup = BeautifulSoup(browser.page_source,"html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
star_names =[]
distance = []
radius = []
lum = []
mass = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][2])
    radius.append(temp_list[i][3])
    lum.append(temp_list[i][4])
    mass.append(temp_list[i][5])

headers = ["star_names","distance","radius","lum","mass"]
df = pd.DataFrame(list(zip(star_names,distance,radius,lum,mass)), columns = headers)
df.to_csv('scraped_data.csv',index = True, index_label="id")