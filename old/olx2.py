#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  web.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import urllib3
from bs4 import BeautifulSoup
import requests

def get_pagina(url) :
	#headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	#html = requests.get(url, headers).content;
	html = requests.get(url).content;
	return html;	
#fim def get_pagina	

def main():
	
	arquivo = open("url.txt", "r");
	arquivoDestino = open("dados_url.txt", "wt");
	
	lstConteudo = [];
	for i in range(10):
		conteudo = arquivo.readline();
		lstConteudo.append(conteudo);
	#for i...
	
	lstHtml = [];
	lstSoup = [];
	
	j=0;
	while (conteudo != '') :	
	
		
		html = get_pagina(conteudo);
		soup = BeautifulSoup(html, "lxml")	
		
		title = soup.findAll('meta', {'property':'og:title'})[0].attrs['content'];
		description = soup.findAll('meta', {'property':'og:description'})[0].attrs['content'];
		image = soup.findAll('meta', {'property':'og:image'})[0].attrs['content'];
		
		arquivoDestino.write(title.encode('utf-8')+";"+description.encode('utf-8')+";"+image);
		arquivoDestino.write("\n");
		
		if (j == 10)
			break;
		#fim if j...
		j += 1;
				
		conteudo = arquivo.readline();
	#fim while...	
	
	arquivo.close();
	arquivoDestino.close();
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
