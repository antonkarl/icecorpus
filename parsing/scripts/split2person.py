# This Python file uses the following encoding: utf-8
# Split 2nd person pronoun from verb stem in labaled bracketing file with one word per line. 
# First argument is input file, second argument is output file.
# Example: "(V-IA2SP heldurðu-halda)" becomes "(V-IA2SP heldur$-halda) (NP-SBJ (PRO $ðu-þú))"
# Anton Karl Ingason, Jan 27 2010. 

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ'
verbMatch = '\(V-([A-Z]{2})2([A-Z]{2}) (.+)(ðu|du|tu)-(['+allchars+']+)\)'

# Open input file for reading
f = open(sys.argv[1], 'r')
linelist = f.readlines()
output = ''

for line in linelist:
	# Find out if this is a verb to split and apply a RegEx replace if a match was found
	if re.search(verbMatch,line) != None:
		tag = re.search(verbMatch,line).group(1)
		tag2 = re.search(verbMatch,line).group(2)
		stem = re.search(verbMatch,line).group(3)
		pro = re.search(verbMatch,line).group(4)
		lemma = re.search(verbMatch,line).group(5)
		fixed = '(V-'+tag+'2'+tag2+' '+stem+'$-'+lemma+') (NP-SBJ (PRO-N $'+pro+'-þú))'
		fixed = re.sub( verbMatch, fixed, line )		
		output = output + fixed 
	else:
		output = output + line 

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()

