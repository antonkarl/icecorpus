# usage: python3 corpuswords2.py "finished/*.psd"

import sys
import re
import glob

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

def strip_sentence(theSentence):
    currentSentence = theSentence
    currentSentence = re.sub("\((CODE|ID) ([A-Z0-9\-\_\,\.\:\?\!\;]+)\)","",currentSentence)
    currentSentence = re.sub("\(([A-Z0-9\+\=\-\,\.\:\?\!\;]+) "," ",currentSentence)
    currentSentence = re.sub("[\)]+"," ",currentSentence)
    currentSentence = re.sub(" (["+allchars+"\-\,\.\:\?\!\;]+)-(["+allchars+"\-\,\.\:\?\!\;]+) "," \\1 ",currentSentence)
    currentSentence = re.sub("[ ]+"," ",currentSentence)
    currentSentence = re.sub("\$ \$","",currentSentence)
    currentSentence = re.sub("\(","",currentSentence)
    currentSentence = re.sub(" (\*(T|ICH)\*\-[0-9]+ )+"," ",currentSentence)
    currentSentence = re.sub(" \*\-[0-9]+ "," ",currentSentence)
    currentSentence = re.sub(" \*(con|arb|pro|exp)\* "," ",currentSentence)
    currentSentence = re.sub(" \* "," ",currentSentence)
    currentSentence = re.sub(" (0 )+"," ",currentSentence)

#    currentSentence = currentSentence.strip()
    return currentSentence.strip()

def count_file(filename):
    f = open(filename, 'r')

    wordCount=0
    lines = f.readlines()
    # print(len(lines))

    currentSentence=""
    displaySentence=""
    for line in lines:
        theLine = line.strip()
        currentSentence = currentSentence + theLine
        displaySentence = displaySentence + line
        if len(line.strip())==0:
            stripped = strip_sentence(currentSentence)
            wordCount = wordCount + len(stripped.split(" "))
            currentSentence=""
            displaySentence=""
    wordCount=wordCount-1
    print(filename + ": " + str(wordCount) )
    return wordCount
# Start script
# Load input file (ipsd)


files=sys.argv[1]

totalCount=1
for file in glob.glob( files ):
    totalCount=totalCount+count_file(file)

print("Total number of words: " + str(totalCount) )
#    if len(line)==0:
#        currentText=""



# Write result to output file
# f = open(sys.argv[1]+".ipsd", 'w')
# f.write(currentText)
# f.close()
