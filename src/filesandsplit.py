#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#libreria para thread
import threading

self = sys.argv[0]
arguments = sys.argv[1:]
"""
threads = list()
for i in range(3):
    t = threading.Thread(target=input_split, args=(i,))
    threads.append(t)
    t.start()
"""
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


def shuffling_reduce(linedict):
	pass


words = input_split(arguments)
