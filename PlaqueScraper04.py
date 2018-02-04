#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup
import json
import re

base_url = "https://online.aberdeencity.gov.uk/Services/CommemorativePlaque/PlaqueDetail.aspx?Id="
file_start = "<htmL><body>"
file_end = "</body></html>"
file_text = ""
data = {} 
data['plaques'] = [] 

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
	pn = ''
	pl = ''
	pa = ''
	pt= ''
	pab = ''
	pm1 = ''
	pm2=''

	if len (paras) == 0:
		pass # do nothing

	elif len(paras) == 8:

		pn = paras[0].text.strip()
		pl = paras[4].text.split(':')[1].strip()
		pa = paras[5].text.split(':')[1].strip()
		pt = paras[6].text.split(':')[1].strip()
		pab = paras[7].text.split(':')[1].strip()

	else: 
		pn = paras[0].text.strip()
		pl = paras[1].text.split(':')[1].strip()
		pa = paras[2].text.split(':')[1].strip()
		pt = paras[3].text.split(':')[1].strip()

		if len (paras) == 5:
			pt = paras[4].text.split(':')[1].strip()

		if len (paras) == 6:
			pt = paras[4].text.split(':')[1].strip()
			pm1 = paras[5].text.split(':')[1].strip()

		if len(paras) == 7:
			pt = paras[4].text.split(':')[1].strip()
			pm1 = paras[5].text.split(':')[1].strip() 
			pm2 = paras[6].text.split(':')[1].strip() 
		
		#file_text = file_start + pn + pl + pa + pt + pab +pm1 + pm2 + file_end
		#file_text = file_text.encode('ascii', 'ignore').decode('ascii')
		
		if pab != '':
			if pm1 != '':
				pab += '\n\n' + pm1
			if pm2 != '':
				pab += '\n\n' + pm2

		pix = aspnet_form.find_all('img')
		pic_list = []

		for pic in pix: 
		
			links = [x['src'] for x in aspnet_form.findAll('img')]
		
			link_no = 0
			for link in links:

				m = re.search ('[a-z0-9]+.jpg', links[link_no], re.IGNORECASE)
				local_name = m.group(0)

				my_url = links [0]
				pic_list.append (local_name)
				# uncomment the following line to download the photos

				# urllib.request.urlretrieve (my_url, "photos/" + local_name)

		data['plaques'].append({  
    	'name': pn, 'location': pl,'area': pa, 'type': pt , 'about': pab, 'photos': pic_list })


		
		# show progress
		'''
		print ("Processing Record " + id_str)
		print ("This is the output:")
		print (file_text)
		print ("\n ###################################### \n")
		'''
		
		#new_file = "plaque" + id_str + ".html"
		#outfile = open(new_file, 'wb')
		#outfile.write(file_text.encode('utf-8'))
		#outfile.close()

x = 1


while x < 115:
	to_scrape = base_url + str(x)
	do_the_scrape(to_scrape, str(x))
	x += 1

with open('plaques.json', 'w') as outfile:
			json.dump(data, outfile)
outfile.close	


