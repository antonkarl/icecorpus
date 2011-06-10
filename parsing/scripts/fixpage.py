#This script uses the encoding utf-8

import sys,string,re

def fixpage(matchobj):
    pagenum = matchobj.group(0).replace("[","(P:")
    pagenum2 = pagenum.replace("]",")")
    return pagenum2

text = sys.stdin.read()
text2 = re.sub("(\[)([0-9]+)(\])",fixpage,text)
sys.stdout.write(text2)
