#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  olx_get_link.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

from bs4 import BeautifulSoup
import requests
import time;
import conect_db_postgre;

def get_pagina(url) :
	headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	html = requests.get(url, headers=headers).content;
	return html;	
#fim def get_pagina	

def main():
	
	url = 'http://es.olx.com.br/imoveis';
	conteudo = "";
	title = "";	
	
	print ("Inicio : %s" % time.ctime());
	
	#arquivo_url = open("url_busca.txt", "w");
	
	html = get_pagina(url);	
	soup = BeautifulSoup(html, "lxml");
	div_search = soup.find('div', {'class':'search-subcategory-nav'});
	li = div_search.findAll('li', {'class':'item'});
				
	for i in li:
		
		link = i.find('a');
		url = link.attrs['href'];
		title = link.attrs['title'];
		
		html = get_pagina(url);	
		soup = BeautifulSoup(html, "lxml");

		id_search = ['types','real_estate_type', 're_land_type', 'season_type', 're_release_type'];
		
		for search in id_search:
			div_real_estate = soup.find('div', {'id': search});

			if (div_real_estate != None) :
				li_item = div_real_estate.findAll('li', {'class':'item'});
				for j in li_item:
					link = j.find('a');
					
					conect_db_postgre.insert_link_search(title.encode('utf-8'), link.get_text().encode('utf-8'), link.attrs['href']);
					
					#conteudo = title.encode('utf-8')+"|"+link.get_text().encode('utf-8')+"|"+link.attrs['href'];
					#arquivo_url.write(conteudo);
					#arquivo_url.write("\n");
					
				#fim j for
			#fim if/else...
					
		#fim for id_search...	
	#fim i for ...	
	
	#arquivo_url.close();
	
	print ("Final: %s" % time.ctime());
	
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
