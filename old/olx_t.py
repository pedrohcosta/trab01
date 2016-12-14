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

import time
import urllib3
from bs4 import BeautifulSoup
import requests
import threading 

def get_pagina(url) :
	#headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	#html = requests.get(url, headers).content;
	html = requests.get(url).content;
	return html;	
#fim def get_pagina	

def extrai_dados(url) :
	html = get_pagina(url);
	soup = BeautifulSoup(html, "lxml")	
		
	title = soup.findAll('meta', {'property':'og:title'})[0].attrs['content'];
	description = soup.findAll('meta', {'property':'og:description'})[0].attrs['content'];
	image = soup.findAll('meta', {'property':'og:image'})[0].attrs['content'];
	
	#print title.encode('utf-8')+";"+description.encode('utf-8')+";"+image;
#fim def extrai_dados	

def main():
	
	arquivo = open("url.txt", "r");
	arquivoDestino = open("dados_url.txt", "wt");
	
	'''
		<meta property="og:title" content="Aptº Colina de Laranjeiras BNN163 - Venda - casas e apartamentos - Colina De Laranjeiras, Serra | bomnegócio agora é OLX.com.br">
		<meta property="og:site_name" content="OLX">
		<meta property="og:url" content="http://es.olx.com.br/norte-do-espirito-santo/imoveis/apt-colina-de-laranjeiras-bnn163-81518736">
		<meta property="og:description" content="Ótimo 2 quartos com armários, sala, banheiro social com box, cozinha com armários, vaga de garagem, esquadrias de alumínio, rebaixamento em gesso, prédio com porteiro físico, play ground, salão de jogos, quadra de esportes, salão de festas, área de lazer. Ótima opção de moradia, bem localizado, próximo a shopping e faculdade. Venha conferir!">
		<meta property="og:image" content="http://img.olx.com.br/images/54/541529039813595.jpg">
	'''
	
	print "%s" % (time.ctime(time.time()) )
	conteudo = arquivo.readline();
	while (conteudo != '') :
		
		x = 0;
		while (conteudo != '' and x < 100) :
			myThread = threading.Thread(target=extrai_dados, args=(conteudo, ))
			myThread.start()
			conteudo = arquivo.readline();	
			arquivoDestino.write(conteudo+"\n");
			x += 1;	
		#fim while
		
		while (threading.active_count() != 1) :
			pass
		#fim while...
		
		conteudo = arquivo.readline();	
		arquivoDestino.write(conteudo+"\n");
		
		#dados = extrai_dados(conteudo);
		#print(dados);
		#arquivoDestino.write(dados+"\n");

		#break
	#fim while...	
	
	print "%s" % (time.ctime(time.time()) )
	arquivo.close();
	arquivoDestino.close();
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
