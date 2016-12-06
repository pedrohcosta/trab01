#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  olx.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>
#  
 
from bs4 import BeautifulSoup
import time;
import conect_db_postgre;
import util;

def main():
	
	print ("Inicio : %s" % time.ctime());
	arquivo = open("url_veiculo.txt", "r");
	
	conteudo = arquivo.readline();
	while (conteudo != '') :	
		
		dic_veiculos = {
			'Tipo_Veiculo': '',
			'Cilindrada':'0',
			'Modelo':'',
			'Ano':'',
			'Marca':'',
			'Combustível': '',
			'Quilometragem':'',
			'Câmbio':'',
			'Portas':'',
			'Município': '',
			'Bairro': '',
			'CEP do imóvel': '',
			'Titulo': '',
			'Valor': '0',
			'Codigo Anuncio': '',
			'Descricao': '',
			'Data': '',
			'Opcionais': ''		
		}
		
		conteudo = conteudo.split("|");
		
		tipo = conteudo[0].strip();
		url = conteudo[1].strip();
		
		print(url);
			
		dic_veiculos['Tipo_Veiculo'] = tipo;	
			
		html = util.get_pagina(url);
		soup = BeautifulSoup(html, "lxml")	
		
		
		titulo = soup.find('h1', {'class': 'OLXad-title'});
		if (titulo != None) :
			titulo = titulo.get_text().strip().encode('utf-8');
		else :
			titulo = "";	
		#fim if...
		
		valor = soup.find('span', {'class': 'OLXad-price'});
		if (valor != None) :
			valor = valor.get_text().strip().encode('utf-8').replace('R$', '');
		else :
			valor = "";	
		#fim if...
		
		codigo_anuncio = soup.find('div', {'class': 'OLXad-id'})
		if (codigo_anuncio != None ) :
			codigo_anuncio = codigo_anuncio.select('p strong')[0].get_text().strip().encode('utf-8');
		else :
			codigo_anuncio = ""
		#fim if...	
		
		descricao = soup.find('div', {'class': 'OLXad-description'});
		if (descricao != None ) :
			descricao = descricao.select('p')[0].get_text().strip();
			descricao = util.limpa_string(descricao.encode('utf-8'));
		else :
			descricao = "";	
		#fim if...
		
		data = soup.find('div', {'class': 'OLXad-date'});
		if (data != None) :
			data = data.select('p')[0].get_text().strip().encode('utf-8').replace('Inserido em: ', '');
		else :
			data = "";	
		#fim if...
		
		caracteristicas = soup.find('div', {'class': 'OLXad-features'});
		if (caracteristicas != None) :
			caracteristicas = caracteristicas.select('p')[0].get_text().strip();
			caracteristicas = util.limpa_string(caracteristicas.encode('utf-8')).replace('Opcionais:', '').replace(', ', ',');
			caracteristicas = caracteristicas.split(',');
		else :
			caracteristicas = [];	
		#fim if...
		
		lst_class = ['OLXad-details', 'OLXad-location', 'OLXad-location-map'];
		
		for class_search in lst_class :
			
			div = soup.find('div', {'class': class_search});
			if (div != None) :
				for el in div.findAll('li') :
					chave = el.select('p span')[0].get_text().strip().replace(':', '');
					chave = chave.encode('utf-8');
					if (chave in dic_veiculos.keys()):
						val_text = el.select('p strong')[0].get_text().strip();
						dic_veiculos[chave] = val_text;
					#fim if...	
					
					if (chave == 'Modelo') :
						val_text = el.select('p strong a')[0].attrs['title'];
						dic_veiculos['Marca'] = val_text;
					#fim if...	
				#fim for i...
			#fim if...
			
		#fim for class_search
			
		
		dic_veiculos['Titulo'] = titulo;
		dic_veiculos['Valor'] = valor;
		dic_veiculos['Codigo Anuncio'] = codigo_anuncio;
		dic_veiculos['Descricao'] = descricao;
		dic_veiculos['Data'] = data;
		
		if (codigo_anuncio != "") :
			
			bairro = conect_db_postgre.insert_bairro(dic_veiculos['Bairro'].encode('utf-8'));
			municipio = conect_db_postgre.insert_municipio(dic_veiculos['Município'].encode('utf-8'));
			
			lst_dados = [];
			lst_dados.append(dic_veiculos['Codigo Anuncio'].replace('\'', '"'));
			lst_dados.append(0); #longitude
			lst_dados.append(0); #longitude
			lst_dados.append(dic_veiculos['Descricao'].replace('\'', '"')); 
			lst_dados.append(dic_veiculos['Titulo'].replace('\'', '"')); 
			lst_dados.append((util.get_numero_string(dic_veiculos['Valor']))); 
			lst_dados.append(util.toDate(dic_veiculos['Data'])); 
			lst_dados.append(dic_veiculos['CEP do imóvel']); 
			lst_dados.append(bairro); 
			lst_dados.append(municipio); 
			
			marca = dic_veiculos['Marca'].encode('utf-8');
			p = marca.rfind(" ");
			marca = marca[:p];
						
			cambio = conect_db_postgre.insert_cambio(dic_veiculos['Câmbio'].encode('utf-8').strip());
			marca = conect_db_postgre.insert_marca(marca);
			modelo = conect_db_postgre.insert_modelo(dic_veiculos['Modelo'].encode('utf-8').strip()[p+1:]);
			combustivel = conect_db_postgre.insert_combustivel(dic_veiculos['Combustível'].encode('utf-8').strip());
			
		
			
			lst_dados.append(tipo); 
			lst_dados.append(int(util.get_numero_string(dic_veiculos['Ano']))); 
			lst_dados.append(int(util.get_numero_string(dic_veiculos['Cilindrada']))); 
			lst_dados.append(int(util.get_numero_string(dic_veiculos['Portas']))); 
			lst_dados.append(float(util.get_numero_string(dic_veiculos['Quilometragem']))); 
			lst_dados.append(modelo); 
			lst_dados.append(marca); 
			lst_dados.append(combustivel); 
			lst_dados.append(cambio); 
			
			veiculo = conect_db_postgre.insert_veiculo(lst_dados);
			
			lst_caracteristica = [];
			for c in caracteristicas:
				caracteristica = conect_db_postgre.insert_opcional(c);
				conect_db_postgre.insert_veiculo_opcional(int(caracteristica), int(veiculo))
			#fim for c...
			
		#fim if...
		
		conteudo = arquivo.readline();
		
		time.sleep(0.3);
	#fim while...	
	
	arquivo.close();
	print ("Final: %s" % time.ctime());
	
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
