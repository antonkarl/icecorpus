#This uses utf-8
#file takes a list of things with each thing on a line and outputs a list separated by pipe

import sys,string

list = sys.stdin.readlines()

for ii in list:
    sys.stdout.write("%s|" % ii)
