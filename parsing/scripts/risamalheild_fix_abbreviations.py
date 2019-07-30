# This Python file uses the following encoding: utf-8

### Converts .lemmatized files such that each incorrectly tokenized abbreviation,
### as specified in the provided abbreviations file,  where the period used at
### the end has been separated from the abbreviation is restored as a single
### token, e.g. hv followed by . is restored to hv.
### The script will also convert the lemma to the unabbreviated form as
### specified in the same abbreviations file.

### Usage:
### python3 risamalheild_fix_abbreviations.py [input file] [output file] [abbreviations file]

### Created by Kristján Rúnarsson

import sys,re

# Define RegEx pattern for characters in tags
tagchars = '0-9a-zþæðöáéýúíó\.-'

# Open abbreviations file
abbrfile = open(sys.argv[3], 'r')
# Create empty dictionary for abbreviations
abbr = {}
# Load abbreviations from file
for line in abbrfile:
    (key, val) = line.split()
    abbr[key] = val
abbrfile.close()

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()
f.close()

# replaces each abbreviation when followed by .
for x in abbr:
    xCap = x.capitalize()
    output = re.sub("^"+x+" ["+tagchars+"]+ ("+x+"|"+xCap+")\n\\. \\. \\.", x+". as "+abbr[x], output, flags=re.MULTILINE)
    # also look for abbreviations with initial capital (as at the start of sentences)
    output = re.sub("^"+xCap+" ["+tagchars+"]+ ("+x+"|"+xCap+")\n\\. \\. \\.", xCap+". as "+abbr[x], output, flags=re.MULTILINE)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
