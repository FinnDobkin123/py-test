#Prepare scraper
import requests
from bs4 import BeautifulSoup
url = "https://www.healthaffairs.org/toc/hlthaff/current"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'pb-page-content')

#Iterate through html of articles
for result in results:
    print(results, end = '\n'*2)
print(results.prettify())
tests = results.find_all('div')
for test in tests:
    print(test.text)
    temp = test.text
    temp2 = temp.split("")

#Put into dataframe
import numpy as np
import pandas as pd
from urllib.request import urlopen
