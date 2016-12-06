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
	
	arquivo_url_destino = open("url_veiculo.txt", "w");
	arquivo_url_busca = open("url_busca.txt", "r");
	
	conteudo = arquivo_url_busca.readline();
	while (conteudo != '') :
		
		conteudo = conteudo.strip();
		if (conteudo != "") :
			
			conteudo = conteudo.split('|');
			url = conteudo[1]+"?";
			i = 0;
			ok = True;
			
			while (ok) :	
				html = get_pagina(url);	
				soup = BeautifulSoup(html, "lxml")	
				links_a = soup.findAll('a', {'class':'OLXad-list-link'})

				for link in links_a :
					arquivo_url_destino.write(conteudo[0]+'|'+link.attrs['href']);
					arquivo_url_destino.write("\n");
				#fim for link ...
				
				li = soup.findAll('li', {'class':'item next'});
				if (len(li) == 0) :#verifica se existem proximo item paginacao
					ok = False;
					continue;
				#fim if...
				
				i += 1;
				url = conteudo[1]+'?o='+str(i);
				print(url);	
				time.sleep(0.5);

			#fim while...			
		#fim if...
		
		print(conteudo);
		conteudo = arquivo_url_busca.readline();
		
	#fim while...	
	
	arquivo_url_destino.close();
	arquivo_url_busca.close();
	
	#url = 'http://es.olx.com.br/imoveis?';
	#i = 0;
		
	
	print ("Final: %s" % time.ctime());
	
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
