import urllib2
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.PhantomJS()
for i in range(1,10):
	url = "https://www.petersons.com/graduate-schools/SearchResults.aspx?q=computer%20science%20master&ct=traditional&deg=masters&aos=includeMissing-false|Computer%20Science&page="+str(i)+"&resultsperpage=60"
	browser.get(url)
	html_source = browser.page_source
	page = html_source.encode('utf-8')
	list_of_school = []
	soup = BeautifulSoup(page, "lxml")

	for links in soup.findAll("h5", class_="inst-dept-name"):
	    for link in links:
	        list_of_school.append(link.get("href"))
	       	
	# print list_of_school[0]

	for school in list_of_school:
		url2 = "https://www.petersons.com" + school
		page = urllib2.urlopen(url2).read()
		soup = BeautifulSoup(page, "lxml")

		count = 0
		apply_tag = []
		apply_stat = []

		if soup.find("span", class_="level3") is not None:
			print soup.find("span", class_="level3").getText().strip()
		else:
			print soup.find("span", class_="level2").getText().strip()
		

		for apply_label in soup.findAll("span", class_="admissions_label"):
			count = count + 1
			apply_tag.append(apply_label.getText().strip())
			if count == 4:
				break

		count = 0
		for apply_data in soup.findAll("span", class_="admissions_data"):
			count = count + 1
			apply_stat.append(apply_data.getText().strip()) 
			if count == 4:
				break

		for index in range(len(apply_tag)):
			if(apply_tag[index] != 'Acceptance Rate'):
				print apply_tag[index]+":", apply_stat[index]
			else:
				if  apply_stat[index] != 'Not Reported':
					print apply_tag[index]+":", apply_stat[index]+"%"
				else:
					print apply_tag[index]+":", apply_stat[index]
		print "\n"


