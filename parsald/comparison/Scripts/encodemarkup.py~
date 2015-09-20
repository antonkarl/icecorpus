# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()

output = re.sub("\(", "danced ", output)

output = re.sub("\)", " placed", output)

output = re.sub("CP ", "compliðurinn ", output)

output = re.sub("NP\*OB1 ", "objectliðurinn ", output)

output = re.sub("NP\*OB2 ", "indobjektliðurinn ", output)

output = re.sub("NP\*SBJ ", "subjectliðurinn ", output)

output = re.sub("NP\*PRD ", "predliðurinn ", output)

output = re.sub("WNP ", "whatliðurinn ", output)

output = re.sub("NP ", "nounliðurinn ", output)

output = re.sub("IP\*INF ", "infinitiveliðurinn ", output)

output = re.sub("IP ", "inflectional ", output)

output = re.sub("PP ", "prepositionliðurinn ", output)

output = re.sub("WADJP ", "wadjiveliðurinn ", output)

output = re.sub("ADJP ", "adjectiveliðurinn ", output)

output = re.sub("WADVP ", "whatviksliðurinn ", output)

output = re.sub("ADVP ", "atviksháborðaliðanna ", output)

output = re.sub("CONJP ", "conjliðurinn ", output)

#heads

output = re.sub("ADJ ", "adjectivehöfuðið ", output)

output = re.sub("ADP ", "adpositionhöfuðið ", output)

output = re.sub("ADV ", "atviksháborðanna ", output)

output = re.sub("CONJ ", "conjhöfuðið ", output)

output = re.sub("DET ", "determinerhöfuðið ", output)

output = re.sub("NOUN ", "nounhöfuðið ", output)

output = re.sub("NUM ", "numberhöfuðið ", output)

output = re.sub("PRON ", "pronhöfuðið ", output)

output = re.sub("PRT ", "particlehöfuðið ", output)

output = re.sub("VERB ", "verbhöfuðið ", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
