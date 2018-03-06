#!/usr/bin/python
# -*- coding: utf-8 -*-

#open file extract data and close file
f = open('a.txt', 'r')
print "Name of the file: ", f.name
data = f.read().replace("\n", " ").replace(".", " ").replace(",", " ")


f.close()

#split the data 
def split_and_dict(data):
	
    # split the text
    words = data.split(" ")

    MyWords = {word:1 for word in words}

    print MyWords
    return

split_and_dict(data)

	