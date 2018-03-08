#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import pprint




# split the data
def input_split():
	# open file extract data and close file
	#for argument in arguments:
	f = open('a.txt', 'r')

	while True:
		data = f.readline(10)
		procesfile = process_data(data)
		linedict = mapping(procesfile)
		outmapping = shuffling_reduce(linedict)

		if not data: break


def process_data(data):

	data = data.lower()
	data = re.sub(r'\W+', '', data)
	"""
				data = data.lower().replace("\n", "").replace(".", "").replace(",", "").replace("!", "").replace("-", "").replace("¡", "")
				data = data.replace("?", "").replace("¿", "").replace("(", "").replace(")", "").replace("  ", " ").replace(";", " ")"""
	data = data.split(" ")

	return data


def mapping(procesfile):
	MyWords = {}
	for valor in procesfile:
		if valor in MyWords:
			MyWords[valor] += 1
		else:
			MyWords[valor] = 1

	return MyWords


final_dict = dict()
def shuffling_reduce(linedict):
	result = {}
	for key in linedict.keys():
		if key not in final_dict:
			final_dict[key] = 1
		else:
			final_dict[key] += 1
			
	return result


resultinput = input_split()

pprint.pprint(final_dict)