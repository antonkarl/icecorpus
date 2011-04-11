#!/usr/bin/python3
#
#  ./tagged2lemmadict filepattern output_file
#  Example: ./tagged2lemmadict.py tagged/*.tagged icepahc.lemmata
#
import glob
import sys
import os
from operator import itemgetter

def extract_lemmata( filename, lemmadict, ambiguous ):
#    print("extracting from " + filename)
    file = open( filename )
    lines = file.readlines()
    for line in lines:
        if len( line.split("\t") ) == 3:
            word, tag, lemma = line.split("\t")
            word = word.lower()
            lemma = lemma.strip().lower()
            
            if lemma != "0":            
                identity = word + "\t" + tag
                if identity in lemmadict.keys():
                    mappings = lemmadict[identity]
                    if lemma in mappings:
                        mappings[lemma] += 1
                    else:
                        ambiguous.add( identity )
                        mappings[lemma] = 1               
                else:                    
                    mappings = {}
                    mappings[lemma] = 1
                    lemmadict[identity] = mappings
            
# get input params
file_matcher = sys.argv[1]  # like something/*.tagged
output_file = sys.argv[2]  #

# create lemmadict
lemmata = {}
ambiguous = set()

# run the extractor on each file matched by file matcher
allfiles = glob.glob( file_matcher )
for file in allfiles:
    print( file )
    extract_lemmata( file, lemmata, ambiguous )
    print( "Lemma identities: "+ str(len(lemmata)) )


lines = []

output = ""
for identity in lemmata:
    mappings = lemmata[identity]
    
    score = 0
    bestmapping = "X"    
    for mapping in mappings.keys():
        if mappings[mapping] > score:
            score = mappings[mapping]
            bestmapping = mapping
                    
    lines.append( identity + "\t" + bestmapping + "\n" ) 

lines = sorted( lines )
print( len(lines ))
output = output.join(lines)

open( output_file, "w" ).write( output )

print( "done" )

