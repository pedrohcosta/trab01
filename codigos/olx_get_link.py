#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  olx_get_link.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import conect_db_postgre;
from bs4 import BeautifulSoup
import requests
import time;

def get_pagina(url) :
	headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	html = requests.get(url, headers=headers).content;
	return html;	
#fim def get_pagina	

def main():
	
	print ("Inicio : %s" % time.ctime());
	
	arquivo_url_destino = open("url.txt", "w");
	rows = conect_db_postgre.select_all_tipo();
	
	for conteudo in rows: 
		url = conteudo[3].strip();
		tipo = conteudo[0];
		url_search = url;
		
		if (url != "") :
			
			i = 0;
			ok = True;
			
			while (ok) :	
			
				html = get_pagina(url);	
				soup = BeautifulSoup(html, "lxml")	
				links_a = soup.findAll('a', {'class':'OLXad-list-link'})

				for link in links_a :
					arquivo_url_destino.write(str(tipo)+'|'+link.attrs['href']);
					arquivo_url_destino.write("\n");
				#fim for link ...
				
				li = soup.findAll('li', {'class':'item next'});
				if (len(li) == 0) :#verifica se existem proximo item paginacao
					ok = False;
					continue;
				#fim if...
				
				i += 1;
				url = url_search+'?o='+str(i);
				print(url);	
				time.sleep(0.5);

			#fim while...
						
		#fim if...
		
 	#fim for...
	
	arquivo_url_destino.close();
	print ("Final: %s" % time.ctime());
	
	return 0
#fim def main

if __name__ == '__main__':
	main();
#fim if...
