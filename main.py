#IMPORTS
from bs4 import BeautifulSoup
import requests
import os

#VARS
url = "https://deadbydaylight.fandom.com/wiki/Shrine_of_Secrets" #URL of page that we will scrape to get info on current Shrine of Secrets
req = requests.get(url)                                          
soup = BeautifulSoup(req.content, 'html.parser')                 #Read content of page and store it
scrape = soup.findAll(class_="sosText")                          #Find all elemets with class "sosText" which are containing surivor/killer and perk names
shrines = []                                                     #Values of only perks
invalids = [1,2,3,4]                                             #Invladis are killer/surivor names which we need to clean out

#Add every element with wanted class to list "shrines"
for x in scrape:
    shrines.append(x)

#Clean out every survior/killer name from the "shrines"
for invalid in invalids:
    shrines.pop(invalid)

#Print every perk without html tags (<></>)
for x in shrines:
    print(x.getText())

#System pause for windows so we can see perks without window closing instantly
os.system("pause")
