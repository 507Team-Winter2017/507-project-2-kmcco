#proj2.py
import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

## Your Problem 1 solution goes here
baseurl = 'http://www.nytimes.com'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")
count = 1
for headline in soup.find_all(class_ = "story-heading"):
	if count <= 10:
		print(headline.get_text().strip())
	count += 1



#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

## Your Problem 2 solution goes here
mdbaseurl = 'https://www.michigandaily.com'
mdr = requests.get(mdbaseurl)
mdsoup = BeautifulSoup(mdr.text, "html.parser")

for title in mdsoup.find_all(class_ = "view-most-read"):
	for child in title.find_all('li'):
		print(child.get_text())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
mnbaseurl = 'http://newmantaylor.com/gallery.html'
mnr = requests.get(mnbaseurl)
mnsoup = BeautifulSoup(mnr.text, 'html.parser')

for img in mnsoup.find_all('img'): 
	if img.has_attr('alt'):
		print(img['alt'])
	else: 
		print("No alternative text provided!")



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
facbaseurl = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
facr = requests.get(facbaseurl, headers={'User-Agent': 'Mozilla/5.0'})
facsoup = BeautifulSoup(facr.text, 'html.parser')

contactpages = []
counter = 0
emails = []

nextpage = [facbaseurl]
for url in nextpage:
	nextr = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	nextsoup = BeautifulSoup(nextr.text, 'html.parser')
	for button in nextsoup.find_all(class_ = 'pager-next last'):
		for a in button.find_all('a'):
			nexturl = 'https://www.si.umich.edu'+a['href']
			nextpage.append(nexturl)

for inst in nextpage:
	rr = requests.get(inst, headers={'User-Agent': 'Mozilla/5.0'})
	instsoup = BeautifulSoup(rr.text, 'html.parser')
	for a in instsoup.find_all('a'):
		if a.get_text() == 'Contact Details':
			contactpages.append(a['href'])

for page in contactpages: 
	pageurl = 'https://www.si.umich.edu'+page
	pager = requests.get(pageurl, headers={'User-Agent': 'Mozilla/5.0'})
	pagesoup = BeautifulSoup(pager.text, 'html.parser')
	for div in pagesoup.find_all(class_ = 'field field-name-field-person-email field-type-email field-label-inline clearfix'):
		for a in div.find_all('a'):
			counter += 1 
			print(str(counter) + " " + a.get_text())

