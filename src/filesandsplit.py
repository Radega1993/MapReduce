#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

self = sys.argv[0]
arguments = sys.argv[1:]
final_dict = dict()


# split the data
def input_split():
    # open file extract data and close file
    for argument in arguments:
        print(argument + ":")
        f = open(argument, 'r')
        final_dict.clear()
        while True:
            data = f.readline(2000)
            process_file = process_data(data)
            line_dict = mapping(process_file)
            shuffling_reduce(line_dict)
            if not data: break
        print_result()


def process_data(data):
    data = data.lower()
    data = re.sub(r'\W+', ' ', data)
    data = data.split(" ")

    return data


def mapping(process_file):
    my_words = {}
    for valor in process_file:
        if valor in my_words:
            my_words[valor] += 1
        else:
            my_words[valor] = 1

    return my_words


def shuffling_reduce(line_dict):
    result = {}
    for key in line_dict.keys():
        if key not in final_dict:
            final_dict[key] = 1
        else:
            final_dict[key] += 1

    return result


def print_result():
    final_dict.pop("")
    for key in final_dict.keys():
        print(key + ' : ' + str(final_dict[key]))
    print('')


input_split()
