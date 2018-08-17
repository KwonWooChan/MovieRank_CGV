import os
from selenium import webdriver
from bs4 import BeautifulSoup

"""
this part for opening brower
"""

driver = webdriver.Firefox()
driver.get('http://www.cgv.co.kr/movies')

"""
check button
"""
button = "//button[@class='btn-more-fontbold']"
driver.find_element_by_xpath(button).click()

html = driver.page_source
driver.close()

root = BeautifulSoup(html, 'html.parser')
mylines = root.find_all('div', class_='sect-movie-chart')
myranks = mylines[0].find_all('li')

rank = 1
for myrank in myranks:
	title = myrank.find('strong', class_='title').text
	print("No." + str(rank) + ': ' +title)
	rank = rank+1

