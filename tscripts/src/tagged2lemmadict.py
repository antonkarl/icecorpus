#!/usr/bin/python3
#
#  ./tagged2lemmadict filepattern output_file
#  Example: ./tagged2lemmadict.py tagged/*.tagged icepahc.lemmata
#
import glob
import sys
import os

def extract_lemmata( filename, lemmadict ):
#    print("extracting from " + filename)
    file = open( filename )
    lines = file.readlines()
    for line in lines:
        if len( line.split("\t") ) == 3:
            word, tag, lemma = line.split("\t")
            identity = word + "_" + tag
            if identity in lemmadict.keys():
                mappings = lemmadict[identity]
                if lemma in mappings:
                    mappings[lemma] += 1
                else:
                    mappings[lemma] = 1               
            else:
                mappings = [{lemma: 1}]
                lemmadict[identity] = mappings
            
# get input params
file_matcher = sys.argv[1]  # like something/*.tagged
output_directory = sys.argv[2]  # like data/

# create lemmadict
lemmata = {}

# run the extractor on each file matched by file matcher
allfiles = glob.glob( file_matcher )
for file in allfiles:
    print( file )
    extract_lemmata( file, lemmata )

for identity in lemmata.keys():
    lemmata[identity]

print( "done" )

