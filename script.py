from bs4 import BeautifulSoup
import re
import requests 


# read urls of websites from text file
links = open("news.txt").read().split("\n")
print (links)
for url in links:
	#store html content of each page
    soup = BeautifulSoup(requests.get(url).text, "html.parser")

#select headlines marked as "h2" 
    articles=soup.findAll("h2")
    for content in articles:
#filer the ones that contain string "orona" (case insensitive)
	    if content.find(text=re.compile("orona")):
	    	thecontent=content
#print the text
	    	print(thecontent.text + "\n" +"THIS IS THE NEXT HEADLINE:")
