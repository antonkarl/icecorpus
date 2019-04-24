# This Python file uses the following encoding: utf-8

### Converts several types of punctuation to markup
### Created by Kristján Rúnarsson

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()
f.close()

# encodes opening and closing parentheses as "(PR:S)" and "(PR:E)", respectively
output = re.sub("\(", "(PR:Sxxxclosingparxxx", output)
output = re.sub("\)", "(PR:E)", output)
output = re.sub("xxxclosingparxxx", ")", output)

# encodes - (HYPHEN-MINUS) – (EN DASH) and — (EM DASH) as "(COM:dash)"
output = re.sub("[-–—]", "(COM:dash)", output)

# encodes both straight and curved apostrophes as "(COM:apostrophe)" 
output = re.sub("['’]", "(COM:apostrophe)", output)

# encodes ellipsis, single character (…) or three periods (...) as "(COM:threedots)"
output = re.sub("(…|\.\.\.)", "(COM:threedots)", output)

output = re.sub("\*", "(COM:asterisk)", output)
output = re.sub("\[", "(COM:openingbracket)", output)
output = re.sub("\]", "(COM:closingbracket)", output)
output = re.sub("\{", "(COM:openingcurlybracket)", output)
output = re.sub("\}", "(COM:closingcurlybracket)", output)

# When three of the same (COM:[something]), (PR:S) or (PR:E) occur, replace
# the second instance with the tag "ta" as if a tagger had tagged  it  after
# running encodemarkup.py. This is to mimic the process in txt2ipsd.sh.
# However, encodemarkup.py will actually be run after this script.
output = re.sub("(\(["+allchars+":]+\)) \1 \1", "\1 ta \1", output)


# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
