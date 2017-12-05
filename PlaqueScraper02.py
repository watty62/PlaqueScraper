#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup


base_url = "https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueDetail.aspx?Id="
file_start = "<htmL><body>"
file_end = "</body></html>"
file_text = ""

def do_the_scrape(inurl, id_str):

	with urllib.request.urlopen(inurl) as url:
		s = url.read()

	soup = BeautifulSoup(s, "lxml")
	pn = ""
	pl = ""
	pa = ""
	pab = ""
	pt = ""
	pm1 = ""
	pm2 = ""
	
	#soup = BeautifulSoup(s, from_encoding="iso-8859-1")

	aspnet_form = soup.find('form')
	
	paras = aspnet_form.find_all('p')

	# the following results from most pages having 5 paras, some 6, one 7, one 8 and a few 0 - i.e. non-existent entries
	
	if len (paras) == 0:
		pass # do nothing

	elif len(paras) == 8:

		pn = '<p id="name">' + paras[0].text.strip() + '</p>'
		pl = '<p id="location">' + paras[4].text.split(':')[1].strip() + '</p>'
		pa = '<p id="area">' + paras[5].text.split(':')[1].strip() + '</p>'
		pt = '<p id="type">' + paras[6].text.split(':')[1].strip() + '</p>'
		pt = '<p id="about">' + paras[7].text.split(':')[1].strip()+ '</p>'

	else: 
		pn = '<p id="name">' + paras[0].text.strip() + '</p>'
		pl = '<p id="location">' + paras[1].text.split(':')[1].strip() + '</p>'
		pa = '<p id="area">' + paras[2].text.split(':')[1].strip()+ '</p>'
		pt = '<p id="type">' + paras[3].text.split(':')[1].strip()+ '</p>'

		if len (paras) == 5:
			pt = '<p id="about">' + paras[4].text.split(':')[1].strip()+ '</p>'

		if len (paras) == 6:
			pt = '<p id="about">' + paras[4].text.split(':')[1].strip() + '</p>'
			pm1 = '<p id="more_info_1">' + paras[5].text.split(':')[1].strip()+ '</p>' 

		if len(paras) == 7:
			pt = '<p id="about">' + paras[4].text.split(':')[1].strip() + '</p>'
			pm1 = '<p id="more_info_1">' + paras[5].text.split(':')[1].strip() + '</p>'
			pm2 = '<p id="more_info_2">' + paras[6].text.split(':')[1].strip() + '</p>'
		
		file_text = file_start + pn + pl + pa + pt + pab +pm1 + pm2 + file_end
		file_text = file_text.encode('ascii', 'ignore').decode('ascii')
		
		# show progress
		'''
		print ("Processing Record " + id_str)
		print ("This is the output:")
		print (file_text)
		print ("\n ###################################### \n")
		'''
		
		new_file = "plaque" + id_str + ".html"
		outfile = open(new_file, 'wb')
		outfile.write(file_text.encode('utf-8'))
		outfile.close()

x = 1

while x < 115:
	to_scrape = base_url + str(x)
	do_the_scrape(to_scrape, str(x))
	x += 1

