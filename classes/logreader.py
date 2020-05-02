#!/usr/local/bin/python3.5
# encoding: utf-8


'''
Created on 12 déc. 2016

@author: home
'''

import re, sys

if __name__ == "__main__":
    file = open(sys.argv[1], 'r')
    for line in file:
        if re.search('recv [1-9][0-9]*', line):
            print (line.split())
        if re.search('^.* del. (?!.*AppleDouble).*$', line):
            print (line.split())