# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()

output = re.sub("danced e", "(", output)

output = re.sub("placed e", ")", output)

output = re.sub("adjectiveliðurinn e", "ADJP", output)

output = re.sub("wadjiveliðurinn e", "WADJP", output)

output = re.sub("compliðurinn e", "CP", output)

output = re.sub("conjliðurinn e", "CONJP", output)

output = re.sub("infinitiveliðurinn nkeng", "IP-INF", output)

output = re.sub("infinitiveliðurinn nkeog", "IP-INF", output)

output = re.sub("objectliðurinn nkeng", "NP-OB1", output)

output = re.sub("indobjektliðurinn nkeng", "NP-OB2", output)

output = re.sub("subjectliðurinn nkeng", "NP-SBJ", output)

output = re.sub("predliðurinn nkeng", "NP-PRD", output)

output = re.sub("nounliðurinn nkeng", "NP", output)

output = re.sub("prepositionliðurinn nkengs", "PP", output)

output = re.sub("prepositionliðurinn nkeng", "PP", output)

output = re.sub("inflectional e", "IP", output)

output = re.sub("atviksháborðaliðanna nkfeg", "ADVP", output)

output = re.sub("atviksháborðaliðanna nhfegö", "ADVP", output)

output = re.sub("whatliðurinn nkeng", "ADVP", output)

#output = re.sub("atviksháborðanna nhfeg", "ADV", output)

output = re.sub("atviksháborðanna nhfeg", "", output)

output = re.sub("adjectivehöfuðið e", "", output)

output = re.sub("adpositionhöfuðið nheog", "", output)

output = re.sub("adpositionhöfuðið nheng", "", output)

output = re.sub("conjhöfuðið e", "", output)

output = re.sub("determinerhöfuðið nheog", "", output)

output = re.sub("determinerhöfuðið nheng", "", output)

output = re.sub("nounhöfuðið nheng", "", output)

output = re.sub("nounhöfuðið nheog", "", output)

output = re.sub("numberhöfuðið nheog", "", output)

output = re.sub("numberhöfuðið nheng", "", output)

output = re.sub("particlehöfuðið e", "", output)

output = re.sub("pronhöfuðið nheog", "", output)

output = re.sub("pronhöfuðið nheng", "", output)

output = re.sub("verbhöfuðið nheng", "", output)

output = re.sub("verbhöfuðið nheog", "", output)

output = re.sub("verbhöfuðið lhensf", "", output)

output = re.sub("verbhöfuðið sfg2fn", "", output)

output = re.sub("verbhöfuðið lheosf", "", output)

output = re.sub("verbhöfuðið ssg", "", output)

#output = re.sub("X nheo", "", output)

#output = re.sub("X nhen", "", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
