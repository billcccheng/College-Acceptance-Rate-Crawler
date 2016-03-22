import urllib2
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Firefox()
# url = "https://www.petersons.com/graduate-schools/SearchResults.aspx?q=texas%20a%26m%20university%20computer%20science&deg=masters&page=1&resultsperpage=60"


# browser.get(url)
# html_source = browser.page_source
# page = html_source.encode('utf-8')
# browser.quit()
# list_of_school = []
# soup = BeautifulSoup(page, "lxml")
# for links in soup.findAll("a0:h5", class_="inst-dept-name"):
#     for link in links:
#         list_of_school.append(link.get("href"))


# # list_of_school = soup.findAll("a0:h5", class_="inst-dept-name")
# print list_of_school[0]

url2 = "https://www.petersons.com/graduate-schools/texas-a-and-m-university-college-of-engineering-department-of-computer-science-000_10040746.aspx"
page = urllib2.urlopen(url2).read()
soup = BeautifulSoup(page, "lxml")

print soup


# print soup
# for link in soup.find_all('a0:a'):
# 	print link.get('href')
