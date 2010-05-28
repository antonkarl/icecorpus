# This Python file uses the following encoding: utf-8
# Split suffixed article from noun stem in labaled bracketing file with one word per line. 
# First argument is input file, second argument is output file.
# Example: "(NP (N-FSDDC sveitinni-sveit)))" becomes "(NP (N-FSDDC sveit$-sveit) (D $inni-hinn)))"
# Anton Karl Ingason, Jan 27 2010. Adapted from a script by Joel Wallenberg.

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ'
nounMatch = '\(N-([A-Z]{3})DC (['+allchars+']+)(inn|inum|ins|inir|ina|inna|in|inni|innar|inar|ið|inu)-(['+allchars+']+)\)'
nounMatch2 = '\(N-([A-Z]{3})DC (['+allchars+']+)(num|ns|nir|n{1,2}a|n{1,2}|nni|n{1,2}ar|ð|nu)-(['+allchars+']+)\)'

# Open input file for reading
f = open(sys.argv[1], 'r')
linelist = f.readlines()
output = ''

for line in linelist:
	# Find out if this word matches one of the two sets of definite nouns
	currentMatch = None
	if re.search(nounMatch,line) != None:
		currentMatch = nounMatch
	elif re.search(nounMatch2,line) != None:
		currentMatch = nounMatch2

	# Apply a RegEx replace if a match was found
	if currentMatch != None:
		tag = re.search(currentMatch,line).group(1)
		case = tag[2]
		stem = re.search(currentMatch,line).group(2)
		article = re.search(currentMatch,line).group(3)
		lemma = re.search(currentMatch,line).group(4)
		fixed = '(N-'+tag+'DC '+stem+'$-'+lemma+') (D-'+case+' $'+article+'-hinn)'
		fixed = re.sub( currentMatch, fixed, line )		
		output = output + fixed 
	else:
		output = output + line 

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
