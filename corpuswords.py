#This Python file uses the following encoding: utf-8

import sys,string,re
from glob import glob

files = sys.argv[1]

count = 0

#loop the whole script over texts in a given directory
for file in glob(files):
    string = open(file,"r").read()
    words = re.findall("[^ \)]\)",string)
    count = count+len(words)

sys.stdout.write("Number of word-level items in files = %s\n\n" % count)
