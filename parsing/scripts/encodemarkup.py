# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()
f.close()

output = re.sub("\(P:([0-9]+)\)", "99xP_\\1x66", output)

output = re.sub("\(MS:(["+allchars+"0-9\_]+)\)", "99xMS_\\1x66", output)

output = re.sub("\(VS:(["+allchars+"0-9\_]+)\)", "99xVS_\\1x66", output)

output = re.sub("\(PR:S\)", "99xPR_Sx66", output)
output = re.sub("\(PR:E\)", "99xPR_Ex66", output)

output = re.sub("\(COM:(["+allchars+"0-9\_]+)\)", "99xCOM_\\1x66", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
