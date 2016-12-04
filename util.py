#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  util.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import requests

def get_pagina(url) :
	headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13'};
	html = requests.get(url, headers=headers).content;
	return html;	
#fim def get_pagina	

def limpa_string(string) :
	nova_string = "";
	for i in string :
		if (i != " ") :
			nova_string += i.strip();
		else :
			nova_string += i;
		#fim if/else	
	#fim for...
	return nova_string		
#fim def limpa_string	

def get_numero_string(string) :
	nova_string = "";
	if (string != "") :
		for i in string :
			if (i in ['1','2','3','4','5','6','7','8','9','0', '', ',']) :
				nova_string += i;
			#fim if/else	
		#fim for...
		return nova_string	
	return "0"	
#fim def limpa_string	

def toDate(data) :
	mes_ext = { 'Janeiro':'01', 'Fevereiro':'02', 'Março':'03',  'Abril':'04', 
	'Maio':'05', 'Junho':'06', 'Julho':'07', 'Agosto':'08', 
	'Setembro':'09', 'Outubro':'10', 'Novembro':'11', 'Dezembro':'12'};
	data = data.split(" ");
	return "2016-"+mes_ext[data[1]]+"-"+data[0];
#fim def...	
