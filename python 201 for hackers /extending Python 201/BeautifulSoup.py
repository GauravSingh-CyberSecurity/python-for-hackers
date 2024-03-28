#web scrapping library 

import requests

page = requests.get("https://247ctf.com/scoreboard")
#print(page.text)

'''
sudo apt install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install beautifulsoup4
pip install requests

'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content,"html.parser")
print(soup.text)
print(soup.title.name)
print(soup.title.string)

print(soup.find("a"))  #this shows the first link in 24ctf.com(website) i.e the dashboard for this case

print("-----------------------------------")
for line in soup.find_all("a"):   #i.e this will show all the links 
    print(line)
    print(line.get('href'))        #href means the place(value) where link is sending you

'''
beautifulsoup converts bunch of  complex html structure into simple
python objects with which we can simply interact with and perform operation as per requirement '''


print("-----------------------------------")

print(soup.find(id= "ferch-error"))
print(soup.find(class_= "nav-link"))
print(soup.find("a",class_="nav-link"))


print("\n\n-----------------------------------")

table = soup.find("table")
#print(table)

table_body = table.find("tbody")
rows = table_body.find_all("tr")

for row in rows:
    print("---")
    #print(row)
    cols = [x.text.strip() for x in row.find_all("td")]
    print(cols)
    print("{} is in {} place with {} points".format(cols[2],cols[0] , cols[4]))

