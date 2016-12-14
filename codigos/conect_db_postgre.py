#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conect_db_postgre.pyc
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import psycopg2

def get_conexao() :
	conn = psycopg2.connect(
			database="trabalho_bd", 
			user="root", 
			password="123456", 
			host="127.0.0.1", 
			port="5432"
	);

	return conn;
#fim def...	

def check_categoria_cadastrada(nome) :
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idcategoria FROM categoria WHERE nome LIKE '"+nome+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	return None;	
#fim def check_categoria_cadastrada	

def insert_categoria(p) :
	conn = get_conexao();
	cur = conn.cursor();
	
	try:
		cur.execute("""INSERT INTO categoria (nome) VALUES (%s) RETURNING idcategoria""", p);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    

#fim def insert_categoria	

def check_tipo_cadastrada(categoria, nome) :
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idtipo FROM tipo WHERE nome = '"+nome+"' AND idcategoria = "+categoria+"");
	rowcount = cur.rowcount;
	if (rowcount > 0) :
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	return None;		
#fim def check_tipo_cadastrada	

def insert_tipo(p) :
	conn = get_conexao();
	cur = conn.cursor();
	
	try:
		cur.execute("""INSERT INTO tipo (idcategoria, nome, url) VALUES (%s, %s, %s)""", p);
		conn.commit();
	except psycopg2.Error as e:
		print (e)
	#fim try/except    

#fim def insert_categoria	

def select_all_tipo() :
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT * FROM tipo");
	rows = cur.fetchall();
	
	return rows;
#fim def select_all_tipo	

def insert_link_search(nome_categoria, nome_tipo, url) :

	result = check_categoria_cadastrada(nome_categoria); 
	if (result == None) :
		result = insert_categoria([nome_categoria]);#retorna ultima id ou None caso erro
		if (result != None) :
			
			result_tipo = check_tipo_cadastrada(str(result), nome_tipo); 
			if (result_tipo == None) :
				insert_tipo([int(result), nome_tipo, url]);#retorna ultima id ou None caso erro
			#fim if...	
		#fim if...	
	else :
		result_tipo = check_tipo_cadastrada(str(result), nome_tipo); 
		
		if (result_tipo == None) :
			insert_tipo([int(result), nome_tipo, url]);#retorna ultima id ou None caso erro
		#fim if...
	#fim if/else...	

#fim def ...	 

def insert_municipio(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idmunicipio FROM municipio WHERE nome LIKE '"+nome.replace('\'', '"')+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se municipio existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO municipio (nome) VALUES (%s) RETURNING idmunicipio""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_municipio	

def insert_bairro(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idbairro FROM bairro WHERE nome LIKE '"+nome.replace('\'', '"')+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO bairro (nome) VALUES (%s) RETURNING idbairro""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_bairro	

def insert_caracteristica(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idcaracteristica FROM caracteristica WHERE nome LIKE '"+nome+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO caracteristica (nome) VALUES (%s) RETURNING idcaracteristica""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_caracteristica	

def insert_imovel_caracteristica(caracteristica, imovel) :
	conn = get_conexao();
	cur = conn.cursor();
	
	try:
		cur.execute("""INSERT INTO imovel_caracteristica(idcaracteristica, idimovel) VALUES (%s, %s);""", [caracteristica, imovel]);
		conn.commit();
	except psycopg2.Error as e:
		print (e);
	#fim try/except    
#fim def insert_caracteristica	

def insert_imovel(lst_dados) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idimovel FROM imovel WHERE idclassificado = (SELECT idclassificado FROM classificado WHERE codigo_anuncio LIKE '"+lst_dados[0]+"')");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO classificado(codigo_anuncio, longitude, latitude, descricao, titulo, 
            valor,  data, cep, idbairro, idmunicipio) 
            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING idclassificado""", lst_dados[:10]);
		res = cur.fetchone();
		last_inserted_id = res[0];
		
		cur.execute("""INSERT INTO imovel(idtipo, area_construida, area_util, vagas_garagem, valor_condominio, 
            quantidade_quartos, iptu, oferta, idclassificado)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING idimovel""", lst_dados[10:]+[last_inserted_id]);
		res = cur.fetchone();
		last_inserted_id = res[0];
		
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_imovel	

def insert_veiculo(lst_dados) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idveiculo FROM veiculo WHERE idclassificado = (SELECT idclassificado FROM classificado WHERE codigo_anuncio LIKE '"+lst_dados[0]+"')");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO classificado(codigo_anuncio, longitude, latitude, descricao, titulo, 
            valor,  data, cep, idbairro, idmunicipio) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING idclassificado""", lst_dados[:10]);
		res = cur.fetchone();
		last_inserted_id = res[0];
		
		cur.execute("""INSERT INTO veiculo(idcategoria, ano, cilindrada, quantidade_porta, quilometragem, 
            idmodelo, idmarca, idcombustivel, idcambio, idclassificado)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING idveiculo""", lst_dados[10:]+[last_inserted_id]);
		res = cur.fetchone();
		last_inserted_id = res[0];
		
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_veiculo	


def insert_cambio(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idcambio FROM cambio WHERE nome LIKE '"+nome+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO cambio (nome) VALUES (%s) RETURNING idcambio""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_cambio	

def insert_combustivel(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idcombustivel FROM combustivel WHERE nome LIKE '"+nome+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO combustivel (nome) VALUES (%s) RETURNING idcombustivel""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_combustivel

def insert_marca(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idmarca FROM marca WHERE nome LIKE '"+nome.replace('\'', '"')+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO marca (nome) VALUES (%s) RETURNING idmarca""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_marca

def insert_modelo(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idmodelo FROM modelo WHERE nome LIKE '"+nome.replace('\'', '"')+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO modelo (nome) VALUES (%s) RETURNING idmodelo""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_marca


def insert_opcional(nome) :
	
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idopcional FROM opcional WHERE nome LIKE '"+nome+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :#verifica se bairro existe 
		rows = cur.fetchall();
		return rows[0][0];
	#fim if...	
	
	try:
		cur.execute("""INSERT INTO opcional (nome) VALUES (%s) RETURNING idopcional""", [nome]);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    
#fim def insert_marca


def insert_veiculo_opcional(opcional, veiculo) :
	conn = get_conexao();
	cur = conn.cursor();
	
	try:
		cur.execute("""INSERT INTO veiculo_opcional(idopcional, idveiculo) VALUES (%s, %s);""", [opcional, veiculo]);
		conn.commit();
	except psycopg2.Error as e:
		print (e);
	#fim try/except    
#fim def insert_veiculo_opcional	

#def main():
		
'''cur.execute("SELECT * FROM categoria")
rows = cur.fetchall()
for row in rows:
	print(row);
#fim for
	'''
#	return 0

#if __name__ == '__main__':
#	main()


