#!/usr/bin/python
# -*- coding: utf-8 -*-

#NIU 1390196 DE ARRIBA GARCIA, RAÜL

import sys
import re

self = sys.argv[0]
arguments = sys.argv[1:]
final_dict = dict()


# take the files
def input():
    # open file extract data and close file
    for argument in arguments:
        print(argument + ":")
        f = open(argument, 'r')
        final_dict.clear()
        while True:
            data = f.readline(2000)
            process_file = process_data_split(data)
            line_dict = mapping(process_file)
            shuffling_reduce(line_dict)
            if not data: break
        print_result()


# proces all the data with lowecase, take out strange characters and split words
def process_data_split(data):
    data = data.lower()
    data = re.sub(r'\W+', ' ', data)
    data = data.split(" ")

    return data


# Mapping the data in a dictionary
def mapping(process_file):
    my_words = {}
    for valor in process_file:
        if valor in my_words:
            my_words[valor] += 1
        else:
            my_words[valor] = 1

    return my_words


# Merging all dict and having a result
def shuffling_reduce(line_dict):
    result = {}
    for key in line_dict.keys():
        if key not in final_dict:
            final_dict[key] = 1
        else:
            final_dict[key] += 1

    return result


# print the result on the console
def print_result():
    final_dict.pop("")
    for key in final_dict.keys():
        print(key + ' : ' + str(final_dict[key]))
    print('')


input()
