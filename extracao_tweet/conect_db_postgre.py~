#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  conect_db_postgre.pyc
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import psycopg2

def get_conexao() :
	conn = psycopg2.connect(
			database="trabalho_twitter", 
			user="root", 
			password="", 
			host="127.0.0.1", 
			port="5432"
	);

	return conn;
#fim def...	

def check_tweets(id) :
	conn = get_conexao();
	cur = conn.cursor();
	
	cur.execute("SELECT idtweets FROM tweets WHERE idtweets LIKE '"+id+"'");
	rowcount = cur.rowcount;
	if (rowcount > 0) :
		return True;
	#fim if...	
	return False;	
#fim def check_tweets	

def insert_tweets(p) :
	conn = get_conexao();
	cur = conn.cursor();
	
	try:
		cur.execute("""INSERT INTO tweets (idtweets, mensagem, data, usuario, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id""", p);
		res = cur.fetchone()
		last_inserted_id = res[0]
		conn.commit();
		return last_inserted_id ;
	except psycopg2.Error as e:
		print (e);
		return None;
	#fim try/except    

#fim def insert_tweets	
