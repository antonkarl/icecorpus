# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ.,$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()

output = re.sub(". . . .", ". .", output)

output = re.sub(". . , ,", ". ,", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
