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

def search_file(query,filename):
    f = open(filename, 'r')

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

            if re.search(query,stripped.lower()):
                print(re.sub(query,'\033[1m'+'\033[91m'+query+'\033[0m',stripped.lower()))
                print(displaySentence)

            currentSentence=""
            displaySentence=""

# Start script
# Load input file (ipsd)


query=sys.argv[1]
files=sys.argv[2]

for file in glob.glob( files ):
    search_file(query, file)


#    if len(line)==0:
#        currentText=""



# Write result to output file
# f = open(sys.argv[1]+".ipsd", 'w')
# f.write(currentText)
# f.close()
