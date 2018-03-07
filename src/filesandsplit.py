#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
#libreria para thread
import multiprocessing

self = sys.argv[0]
arguments = sys.argv[1:]

#split the data 
def input_split(arguments, chunk_size=1024):

	#open file extract data and close file
	for argument in arguments:
		f = open(argument, 'r')
	
	while True:
		data = f.read(chunk_size)
		procesfile = process_data(data)
		linedict = mapping(procesfile)
		if not data: break


def process_data(data):

	data = data.lower().replace("\n", " ")
	data = re.sub(r"[\.\,\;\:\l']", '', data)
	data = data.split(" ")

	return data

def mapping (procesfile):

	MyWords = {}
	for valor in procesfile:
		if valor in MyWords:
			MyWords[valor] += 1
		else:
			MyWords[valor] = 1

	if MyWords.has_key(''):
		del MyWords['']

	print  MyWords
	return MyWords


def shuffling_reduce(linedict):
	result = {}
	for word in linedict:
		if word in result:
			result[word] += 1
		else:
			result[word] = 1
	print  result
	return result   

resultinput = input_split(arguments)
outmapping = shuffling_reduce(linedict)
