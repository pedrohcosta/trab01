#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  teste_conexao.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

#import MySQLdb
import MySQLdb;

def get_conexao() :
	conexao = MySQLdb.connect(
						host='localhost' , 
						user='root' , 
						passwd ='123456', 
						db ='teste_banco',
						charset ='utf8',
						use_unicode=True);
	#conexao.select_db('teste_banco')
	return conexao;
#fim def...	

def gravar_imoveis(cursor, dic) :
	sql = "INSERT INTO imoveis(categoria, tipo, titulo, valor, codigo_anuncio, descricao, data, caracteristica, ";
	sql += " condominio, iptu, area_construida, quartos, vagas_garagem, area_util, minicipio, bairro, cep, latitude, longitude) ";
	sql += " VALUES ('"+dic['Categoria']+"', '"+dic['Tipo_Imovel']+"', '"+dic['Titulo'].replace('\'', '"')+"', '"+dic['Valor']+"', '"+dic['Codigo Anuncio']+"', ";
	sql += " '"+dic['Descricao'].replace('\'', '"')+"','"+dic['Data']+"','"+dic['Caracteristicas'].replace('\'', '"')+"', ";
	sql += " '"+dic['Condomínio']+"','"+dic['IPTU']+"','"+dic['Área construída']+"','"+dic['Quartos']+"',";
	sql += " '"+dic['Vagas na garagem']+"', '"+dic['Área útil']+"', '"+dic['Município']+"', '"+dic['Bairro']+"', ";
	sql += " '"+dic['CEP do imóvel']+"', '0', '0')";
	
	
	try:
		cursor.execute(sql);
	except MySQLdb.Warning, w:
		print(w);
	except MySQLdb.Error, e:
		print ("Erro executando \n " + sql);
		print (e);
	#fim try/except    
	
#fim def

'''def main():
	conexao = get_conexao() ;
	cursor = conexao.cursor();
	
	#gravar_imoveis(cursor, "Descricao Teste: ", 30);
	
	for i in range(10) :
		gravar_imoveis(cursor, "Descricao Teste: "+str(i), (10+i)); 
	#for i...
	
	conexao.commit();	
	
	
	return 0;
#fim def main

if __name__ == '__main__':
	main()
#fim if..	

'''
