#install BeautifulSoup4, requests, 

from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import requests
import string
import re

#parse xml file
tree = ET.parse('NCT01625234.xml')
root = tree.getroot()
eligibility = tree.find("eligibility")
criteria = eligibility.find("criteria")
textblock = criteria.find("textblock")
text = ET.tostring(textblock)
#List of strings of each criteria in the eligibility element
crit_list = re.split('\d+[.] ', text) #crit_list = re.split('\d+\.\w*.', text)

#Get list of biomarkers. Sample from fda.gov
url = "http://www.fda.gov/drugs/scienceresearch/researchareas/pharmacogenetics/ucm083378.htm"
request = requests.get(url)
html = request.text
soup = BeautifulSoup(html)
table = soup.find_all("tbody")
td = soup.find_all("td")
list_of_biomarkers = []
for data in td:
	if(re.search('[A-Z]{2,}',str(data))):
		index = string.find(data.text," ")
		marker = data.text[:index]
		marker = string.strip(marker)
		list_of_biomarkers.append(marker)


for criteria in crit_list:
	#if there is something that looks like a biomarker...
	if(re.search('[A-Z]{2,}',criteria)):
		#check if it contains something in our list of biomarkers
		if any(marker in criteria for marker in list_of_biomarkers):
			print criteria




