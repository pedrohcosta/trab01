#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  olx_get_link.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import urllib3
from bs4 import BeautifulSoup
import requests
import time;

def get_pagina(url) :
	headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	html = requests.get(url, headers=headers).content;
	return html;	
#fim def get_pagina	

def main():
	
	arquivo = open("url.txt", "w");
	url = 'http://es.olx.com.br/imoveis?';
	i = 0;
	
	print ("Inicio : %s" % time.ctime());
	
	while (True) :	
		html = get_pagina(url);	
		soup = BeautifulSoup(html, "lxml")	
		links_a = soup.findAll('a', {'class':'OLXad-list-link'})

		for link in links_a :
			arquivo.write(link.attrs['href']);
			arquivo.write("\n");
		#fim for link ...
		
		li = soup.findAll('li', {'class':'item next'});
		if (len(li) == 0) :#verifica se existem proximo item paginacao
			return;
		#fim if...
		
		i += 1;
		url = 'http://es.olx.com.br/imoveis?o='+str(i);
		print(url);	
		time.sleep(0.5);

	#fim while...	
	
	arquivo.close();
	print ("Final: %s" % time.ctime());
	
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
