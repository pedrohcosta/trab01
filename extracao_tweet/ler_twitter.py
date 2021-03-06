#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ler_twitter.py
#  
#  Copyright 2016 Pedro Henrique <pedro@pedroBook>

import tweepy;
import conect_db_postgre;

def get_tweet(query, api) :
	
	#realizado a chamada do metodo api.search
	#q = query de busca
	#lang ='pt' apenas resultados em pt
	#items(1500) = quantidade de itens retornados
	
	i = 0;
	for tweet in tweepy.Cursor(api.search, q=query, lang='pt').items(15000):
		
		idtweets = tweet.id;#id tweets
		mensagem = tweet.text; #mensagem 
		data = tweet.created_at; #data criação
		usuario = tweet.user.screen_name;#nome usuário
	
		if (tweet.place != None) :#cordenadas latitude/longitude do tweets
			latitude = tweet.place.bounding_box.coordinates[0][0][0];
			longitude = tweet.place.bounding_box.coordinates[0][0][1];			
		#fim if...
		
		if (tweet.coordinates != None) :
			latitude = tweet.coordinates['coordinates'][0];
			longitude = tweet.coordinates['coordinates'][1];	
		#fim if...	
		
		if (tweet.place != None or tweet.coordinates != None) : 
			if (not conect_db_postgre.check_tweets(str(idtweets))) :#verifica que id do tweets já está inserido
				lst = [str(idtweets), mensagem, str(data), usuario, latitude, longitude];
				#print(lst);
				
				conect_db_postgre.insert_tweets(lst);#realiza inserção do tweets
			#fim if...
		#fim if...
		i += 1;		
	#fim for...
	print(i)
#fim def get_tweet...	

def main():
	
	API_KEY = "";
	API_SECRET = "";
	ACCESS_TOKEN = "";
	ACCESS_TOKEN_SECRET = "";
	
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	query = "imovel";
	get_tweet(query, api);
	
			
	return 0
#fim def main

if __name__ == '__main__':
	main()
#fim if...
