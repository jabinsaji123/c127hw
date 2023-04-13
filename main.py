from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Edge("msedgedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Proper_name","Distance","Spectral_class","Mass","Radius","Luminosity"]
    star_data = []
    for i in range(0, 428):
        while True :
         time.sleep(2)  
         soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("ul", attrs={"class", "headerSort"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()