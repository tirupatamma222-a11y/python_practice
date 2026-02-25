

import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.flipkart.com/search?q=mi%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)

'''soup=BeautifulSoup(response.content,'html.parser')
print(soup)'''