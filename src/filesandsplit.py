#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
"""
Print sys.argv[0] # devuelve el nombre del archivo.
Print sys.argv[1] # devuelve el primer argumento en este caso "hola"
Print sys.argv[2] # devuelve elsegundo argumento en este caso "mundo"
"""
self = sys.argv[0]
arguments = sys.argv[1:]



#split the data 
def input_split(arguments):
	
	#open file extract data and close file
	for argument in arguments:
		f = open(argument, 'r')

	while True:
		line = f.readline().lower().replace("\n", " ").replace(".", " ").replace(",", " ").replace("l'", " ")
		words = line.split(" ")
		linedict = mapping(words)
		if not line: break

	f.close()

	return 



def mapping (words):

	MyWords = {word:1 for word in words}
	if MyWords.has_key(''):
		del MyWords['']

	print  MyWords
	return MyWords


def shuffling_reduce():
	pass


words = input_split(arguments)
