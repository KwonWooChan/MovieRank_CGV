import os
import requests
from bs4 import BeautifulSoup

"""
this part for opening brower
"""
r = requests.get('http://www.cgv.co.kr/movies')

html = r.content

root = BeautifulSoup(html, 'html.parser')
mylines = root.find_all('div', class_='sect-movie-chart')
myranks = mylines[0].find_all('li')

rank = 0
for rank in range(0, 8):
	if rank == 7:
		break
	title = myranks[rank].find('strong', class_='title').text
	print("No." + str(rank+1) + ': ' +title)

