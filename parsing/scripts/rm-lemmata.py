import sys
import re
import glob

allchars = 'a-zA-Z0-9þæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\*\"\,\.\:$\{\}\_\<\>\/'

f = open(sys.argv[1], 'r')
text = f.read()
text = re.sub("\(([A-Z0-9\-]+) (["+allchars+"]+)-(["+allchars+"]+)\)","(\\1 \\2)",text)
print(text)
