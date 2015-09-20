#This is an updated version of rm-lemmata.py, created for the project "Vélræn þáttun"

import sys
import re
import glob

allchars = 'a-zA-Z0-9þæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\*\"\,\.\;\:\?\!\$\{\}\_\<\>\/'

f = open(sys.argv[1], 'r')
text = f.read()
text = re.sub("(["+allchars+"]+)-(["+allchars+"]+)","\\1",text)
text = re.sub("(["+allchars+"]+)-(["+allchars+"]+)","\\1",text)
#text = re.sub("(["+allchars+"]+)/(["+allchars+"]+)","\r",text)
print(text)
