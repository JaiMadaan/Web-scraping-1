from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome('C:/Users/cp/OneDrive/Desktop/WhitehatJr/venv/chromedriver')

def scrape():
    headers=["Name","Distance","Mass","Radius"]
    stars=[]
    for i in range(0,203):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","table"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index==0 :
                    temp_list.append(li_tag.find_all('a')[0],contents[0])

                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')

            stars.append(temp_list)
            print(temp_list)
        browser.find_element(by=By.XPATH, value="//*[@id='mw-content-text']/div[1]/table").click()

        #element=findElement(By.xpath("//[@test-id='test-username']"))
    with open("scraper_2.csv","w")as f :
        csvwriter=csv.writer(f) 
        csvwriter.writerow(headers)
        csvwriter.writerows(stars)


scrape()       
