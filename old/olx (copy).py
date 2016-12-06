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

def add_item_linha(dic) :
	linha = '';
	l = len(dic.keys());
	i = 0;
	
	for el in dic.values() :
		linha += el;
		if (i < (l-1)) :
			linha += '||';
		#fim if...
		i += 1;	
	#fim for el
	return linha;	
#fim def add_item_linha	

def main():
	
	arquivo = open("url.txt", "r");
	arquivo_dados = open("dados_url.txt", "wt");
	
	dic_detalhe = {
	'Tipo': '',
	'Condomínio': '',
	'IPTU': '',
	'Área construída': '',
	'Quartos': '',
	'Vagas na garagem': '',
	'Área útil': ''
	};
	
	dic_endereco = {
		'Município': '',
		'Bairro': '',
		'CEP do imóvel': ''
	};
	
	dic_imoveis = {
		'Categoria':'',
		'Tipo_Imovel': '',
		'Condomínio': '',
		'IPTU': '',
		'Área construída': '',
		'Quartos': '',
		'Vagas na garagem': '',
		'Área útil': '',
		'Município': '',
		'Bairro': '',
		'CEP do imóvel': '',
		'Titulo': '',
		'Valor': '',
		'Codigo Anuncio': '',
		'Descricao': '',
		'Data': '',
		'Caracteristicas': ''		
	}
	
	#conexao = conect_db.get_conexao();
	#cursor = conexao.cursor();
	
	conteudo = arquivo.readline();
	while (conteudo != '') :	
		
		dic_imoveis = {
			'Tipo_Imovel': '',
			'Condomínio': '',
			'IPTU': '',
			'Área construída': '',
			'Quartos': '',
			'Vagas na garagem': '',
			'Área útil': '',
			'Município': '',
			'Bairro': '',
			'CEP do imóvel': '',
			'Titulo': '',
			'Valor': '',
			'Codigo Anuncio': '',
			'Descricao': '',
			'Data': '',
			'Caracteristicas': ''		
		}
		
		conteudo = conteudo.split("|");
		
		#print conteudo;
		
		categoria = conteudo[0].strip();
		tipo_imoveis = conteudo[1].strip();
		url = conteudo[2].strip();
		
		dic_imoveis['Categoria'] = categoria;
		dic_imoveis['Tipo_Imovel'] = tipo_imoveis;	
			
		html = get_pagina(url);
		soup = BeautifulSoup(html, "lxml")	
		
		titulo = soup.findAll('h1', {'class': 'OLXad-title'});
		if (len(titulo) > 0) :
			titulo = titulo[0].get_text();
		else :
			titulo = "";	
		#fim if...
		
		valor = soup.findAll('span', {'class': 'OLXad-price'});
		if (len(valor) > 0) :
			valor = valor[0].get_text();
		else :
			valor = "";	
		#fim if...
		
		
		
		codigo_anuncio = soup.findAll('div', {'class': 'OLXad-id'})
		if (len(codigo_anuncio) > 0 ) :
			codigo_anuncio = codigo_anuncio[0].select('p strong')[0].get_text();
		else :
			codigo_anuncio = ""
		#fim if...	
		
		descricao = soup.findAll('div', {'class': 'OLXad-description'});
		if (len(descricao) > 0 ) :
			descricao = descricao[0].select('p')[0].get_text();
			descricao.encode('utf-8');
		else :
			descricao = "";	
		#fim if...
		
		data = soup.findAll('div', {'class': 'OLXad-date'});
		if (len(data) > 0) :
			data = data[0].select('p')[0].get_text();
		else :
			data = "";	
		#fim if...
		
		caracteristicas = soup.findAll('div', {'class': 'OLXad-features'});
		if (len(caracteristicas) > 0) :
			caracteristicas = caracteristicas[0].select('p')[0].get_text();
			caracteristicas.encode('utf-8');
		else :
			caracteristicas = ""	
		#fim if...
		
		#informacoes detalhes
		div = soup.findAll('div', {'class':'OLXad-details'});
		if (len(div) > 0) :
			for el in div[0].findAll('li') :
				chave = el.select('p span')[0].get_text().strip().replace(':', '');
				chave = chave.encode('utf-8');
				if (chave in dic_imoveis.keys()):
					val_text = el.select('p strong')[0].get_text().strip();
					dic_imoveis[chave] = val_text;
				#fim if...	
			#fim for i...
		#fim if...
		
		#informacoes endereco
		div = soup.findAll('div', {'class':'OLXad-location'});
		if (len(div) > 0) :
			for el in div[0].findAll('li') :
				chave = el.select('p span')[0].get_text().strip().replace(':', '');
				chave = chave.encode('utf-8');
				if (chave in dic_imoveis.keys()):
					val_text = el.select('p strong')[0].get_text().strip();
					dic_imoveis[chave] = val_text;
				#fim if...	
			#fim for i...
		#fim if...
		
		div = soup.findAll('div', {'class':'OLXad-location-map'});
		if (len(div) > 0) :
			for el in div[0].findAll('li') :
				chave = el.select('p span')[0].get_text().strip().replace(':', '');
				chave = chave.encode('utf-8');
				if (chave in dic_imoveis.keys()):
					val_text = el.select('p strong')[0].get_text().strip();
					dic_imoveis[chave] = val_text;
				#fim if...	
			#fim for i...
		#fim if...
		
					
		'''linha = '';	
		linha = titulo.strip()+"||"+valor.strip()+'||'+codigo_anuncio.strip()+'||'+data.strip(); 
		linha += "||"+add_item_linha(dic_detalhe);
		linha += "||"+add_item_linha(dic_endereco);
		linha += "||"+descricao.strip();
		linha = linha.encode('utf-8');	
		arquivo_dados.write(linha+"\n");
		'''
		
		dic_imoveis['Titulo'] = titulo;
		dic_imoveis['Valor'] = valor;
		dic_imoveis['Codigo Anuncio'] = codigo_anuncio;
		dic_imoveis['Descricao'] = descricao;
		dic_imoveis['Data'] = data;
		dic_imoveis['Caracteristicas'] = caracteristicas;
		
		
		'''if (codigo_anuncio != "") :
			conect_db.gravar_imoveis(cursor, dic_imoveis); 
			conexao.commit();
		#fim if...
		'''
		
		print dic_imoveis;
		
		#print(valor)
		conteudo = arquivo.readline();
		
		break;
		time.sleep(0.3);
	#fim while...	
	
		
	'''print(dic_detalhe);
	print(dic_endereco);
	print(valor);
	print(descricao);
	print(codigo_anuncio);
	'''
	
	arquivo.close();
	arquivo_dados.close();
	
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
