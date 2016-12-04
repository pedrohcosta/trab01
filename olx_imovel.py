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
import os.path;

def main():
	
	print ("Inicio : %s" % time.ctime());
	arquivo = open("url.txt", "r");
	
	'''if (os.path.isfile('arquivo_posicao.txt')) :#caso arquivo exista
		arquivo_posicao = open("arquivo_posicao.txt","r");
		conteudo_posicao = arquivo_posicao.readline();
		if (conteudo_posicao.strip() != "") :
			arquivo.seek(int(conteudo_posicao), 1);	
		else : 
			arquivo.seek(0, 1);	
		#fim if/else...
		arquivo_posicao.close()
	else :
		arquivo.seek(0, 1);
	#fim if/else...
	'''
	conteudo = arquivo.readline();
	while (conteudo != '') :	
		
		dic_imoveis = {
			'Tipo_Imovel': '',
			'Condomínio': '0',
			'IPTU': '0',
			'Área construída': '0',
			'Quartos': '0',
			'Vagas na garagem': '0',
			'Área útil': '0',
			'Município': '',
			'Bairro': '',
			'CEP do imóvel': '',
			'Titulo': '',
			'Valor': '0',
			'Codigo Anuncio': '',
			'Descricao': '',
			'Data': '',
			'Caracteristicas': ''		
		}
		
		conteudo = conteudo.split("|");
		
		tipo_imovel = conteudo[0].strip();
		url = conteudo[1].strip();
		
		print(url);
			
		dic_imoveis['Tipo_Imovel'] = tipo_imovel;	
			
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
			caracteristicas = util.limpa_string(caracteristicas.encode('utf-8')).replace('Características:', '').replace(', ', ',');
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
					if (chave in dic_imoveis.keys()):
						val_text = el.select('p strong')[0].get_text().strip();
						dic_imoveis[chave] = val_text;
					#fim if...	
				#fim for i...
			#fim if...
			
		#fim for class_search
			
		
		dic_imoveis['Titulo'] = titulo;
		dic_imoveis['Valor'] = valor;
		dic_imoveis['Codigo Anuncio'] = codigo_anuncio;
		dic_imoveis['Descricao'] = descricao;
		dic_imoveis['Data'] = data;
		
		if (codigo_anuncio != "") :
			
			bairro = conect_db_postgre.insert_bairro(dic_imoveis['Bairro'].encode('utf-8'));
			municipio = conect_db_postgre.insert_municipio(dic_imoveis['Município'].encode('utf-8'));
			
			lst_dados = [];
			lst_dados.append(dic_imoveis['Codigo Anuncio'].replace('\'', '"'));
			lst_dados.append(0); #longitude
			lst_dados.append(0); #longitude
			lst_dados.append(dic_imoveis['Descricao'].replace('\'', '"')); 
			lst_dados.append(dic_imoveis['Titulo'].replace('\'', '"')); 
			lst_dados.append((util.get_numero_string(dic_imoveis['Valor']))); 
			lst_dados.append(util.toDate(dic_imoveis['Data'])); 
			lst_dados.append(dic_imoveis['CEP do imóvel']); 
			lst_dados.append(bairro); 
			lst_dados.append(municipio); 
			
			lst_dados.append(tipo_imovel); 
			lst_dados.append(float(util.get_numero_string(dic_imoveis['Área construída']))); 
			lst_dados.append(float(util.get_numero_string(dic_imoveis['Área útil']))); 
			lst_dados.append(int(util.get_numero_string(dic_imoveis['Vagas na garagem']))); 
			lst_dados.append(float(util.get_numero_string(dic_imoveis['Condomínio']))); 
			lst_dados.append(int(util.get_numero_string(dic_imoveis['Quartos']))); 
			lst_dados.append(float(util.get_numero_string(dic_imoveis['IPTU'])));
			lst_dados.append(0);# oferta
			
			imovel = conect_db_postgre.insert_imovel(lst_dados);
			
			#print imovel
			#return 
			
			
			lst_caracteristica = [];
			for c in caracteristicas:
				caracteristica = conect_db_postgre.insert_caracteristica(c);
				conect_db_postgre.insert_imovel_caracteristica(int(caracteristica), int(imovel))
			#fim for c...
			
			#arquivo_posicao = open("arquivo_posicao.txt","w");
			#arquivo_posicao.write(str(arquivo.tell())+"\n");
			#arquivo_posicao.close();
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
