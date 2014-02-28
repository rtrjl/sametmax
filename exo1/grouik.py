#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys
import unicodedata
from collections import defaultdict

	
		
	

def proceed(filename):
	f = open(filename)
	string = f.read()
	string = string.strip()
	string = string.replace("-", " ")
	string = string.replace("’", " ")
	string = string.replace(":", " ")
	string = string.replace(",", "")
	string = string.replace(".", "")
	string = string.replace("	", "")
	string = string.replace("œ", "oe")
	string = string.replace("!", "")
	string = string.replace("?", "")
	string = string.replace("\n", " ")
	string = string.replace("\r", " ")
	string = string.strip()
	string = string.decode("utf-8")
	string = unicodedata.normalize('NFKD', string)
	string = string.encode('ASCII', 'ignore')
	string = string.strip().lower()
	tabword = string.split(" ")
	

	dictword = defaultdict(list)
	position = 0
	for word in tabword:
		if word == "":
			continue
		dictword[word].append(position)
		position +=1
	
	for key,value in sorted(dictword.iteritems(), key = lambda (k,v):(len(v),v)):
		print "%s: %s" % (key,value)

	for item in dictword.iteritems():
		print item
		
		


if __name__ == "__main__":
   proceed(sys.argv[1])
