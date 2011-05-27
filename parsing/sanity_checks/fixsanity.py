#This script uses the encoding utf-8

import sys,string,re

from glob import glob

def fixcommand(matchobj):
    command = matchobj.group(1).replace("append_label","add_leaf_before")
    result = matchobj.group(2).replace("-","_")
    result1 = re.sub("^_","",result)
    wholething = "%s (CODE *%s*)" % (command,result1)
    return wholething

for file in glob('*.q'):
    text = open(file,"r").read()
    text2 = re.sub("(append_label\{1\}:) (.*ZZZ.*)",fixcommand,text)
    output = open(file,"w")
    output.write(text2)
