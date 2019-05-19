import requests
from bs4 import BeautifulSoup

#establish connection with the website
r=requests.get("http://example.webscraping.com/places/default/index/2") 

#get the html file of the wensite
c=r.content

#arrange it in human readable HTML sequence - optional step
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify)

#find the nesting of the tags in which your data is typed
div = soup.find("div",{"id":"results"}) #look for div tags with an 'id' value = 'results'
# print(div) 
# print("<---------------------------------------------------->")
tab=div.find("table")             		    #in those divs look for table tags
# print(tab)
# print("<---------------------------------------------------->")

tr=tab.find_all("tr")                       #in those tables look for tr tags
# print(tr)
# print("<---------------------------------------------------->")

for i in range(5):
	td=tr[i].find_all("td")                 #in those tr tags look for td tags
	#print(td)
	for i in range(2):
		divv=td[i].find("div")              #in those td tags look for div tags
		print(">>>>>>>>>>"+divv.text)       #print the text value associated with the div tags
