#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:33:59 2020

@author: johnzhang
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np



url = f"https://www.basketball-reference.com/teams/LAL/2020/gamelog/"

html = urlopen(url)

soup = BeautifulSoup(html, features= "lxml")

# use findALL() to get the column headers
soup.findAll('tr', limit=2)

# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]



# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
# avoid the first header row
rows = soup.findAll('tr')[3:]
team_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows)-1)]

lakers = pd.DataFrame(team_stats, columns = headers)
lakers.to_csv('laker_data.csv', mode='w', index=False, header=True)

