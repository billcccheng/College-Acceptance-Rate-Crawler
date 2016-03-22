# -*- coding: utf-8 -*-
import urllib2
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_school():
	school_list = []
	for page in range(4,5):
		url2 = "http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-science-schools/computer-science-rankings/page+"+str(page)
		page = urllib2.urlopen(url2).read()
		soup = BeautifulSoup(page, "lxml")
		
		for schools in soup.findAll("a", class_="school-name"):
			school_list.append(schools.getText()) 

		# for school in school_list:
		# 	print school.encode('utf-8')

	return school_list

def get_stats(school_list):
	list_of_school = []
	for school in school_list:
		browser = webdriver.PhantomJS()
		school  = school.encode('utf-8').replace(" ", "%20").replace("—​", " ").replace("-", " ")
		url = "https://www.petersons.com/graduate-schools/SearchResults.aspx?q="+school+"&ct=traditional&deg=masters&aos=includeMissing-false|Computer%20Science&page=1&resultsperpage=20"
		browser.get(url)
		html_source = browser.page_source
		page = html_source.encode('utf-8')
		soup = BeautifulSoup(page, "lxml")
		temp_link = soup.find("h5", class_="inst-dept-name")
		if temp_link is not None:
			link = temp_link.find("a").get("href")
			print_stats(link)
		browser.quit()


def print_stats(link):
	url2 = "https://www.petersons.com" + link
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


if __name__ == "__main__":
	get_stats(get_school())
