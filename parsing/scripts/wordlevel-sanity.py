# 
# Usage:
# python3 path-to-scripts/wordlevel-sanity.py filename
#
# Example (from inside "parsing"):
# python3 scripts/wordlevel-sanity.py jonsteingrims05.anton.psd
#
import sys
import re
# import glob
# Define RegEx patterns for Icelandic characters
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ$'
anything = "["+allchars+"]+"
# word="["+allchars+"]+"

# Required tag for word-lemma pattern
# IMPORTANT, THE ORDER IS ALWAYS: TAG, WORD, LEMMA, MESSAGE
# copy an existing line and change it to avoid typos

# In this section the program complains if the word-lemma pattern is matched but the tag is not matched
req_tag=[]
req_tag.append( ("ONE\+Q\-[NADG]",anything,"einhver","should be tagged ONE+Q-CASE") )
req_tag.append( ("Q\+NUM\-[NADG]",anything,"hvortveggja","should be tagged Q+NUM-CASE") )
req_tag.append( ("OTHER[S]*-[NADG]",anything,"annar","should be tagged OTHER/OTHERS-CASE unless it clearly means the ordinal number 'second' in context") )
req_tag.append( ("C","sem","sem","sem should be tagged C") )
req_tag.append( ("RP","upp|inn|fram|út","\\2","should be tagged RP") )
req_tag.append( ("ALSO","einnig|einninn|einnin","\\2","should be tagged ALSO") )
req_tag.append( ("SUCH",anything,"þvílíkur|slíkur|svoddan","should be tagged ALSO") )

# In this section the program complains if the tag-word pattern is matchec but the lemma is not matched
req_lemma=[]
req_lemma.append( ("NEG","eigi","ekki","lemma for NEG eigi is ekki") )

# In this section the program complains if all the fields are matched
bad=[]
bad.append( ("VB\S*",anything,"(út|inn)([a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ]+)a","should a particle be split off here?") )

# bad.append( ("[^C]","sem","sem","sem should be C") )
# bad.append( ("[^R]\S*","upp|inn|fram|út","\\2","should be RP") )
# bad.append( ("ADJ[RS]*-\S|PRO-\S",".*","þvílíkur|slíkur|svoddan","should be tagged SUCH") )

# End of bad patterns

def process_sentence(sentence,line_local):
	sentenceID="NO_ID" 
	if re.search("\(ID (.*)\)",sentence):
		sentenceID = re.search("\(ID (.*)\)",sentence).group(0)
	sentence_report=""

	lines=sentence.splitlines()
	local_count=0
	for line in lines:
		line_local+=1
		local_count+=1
		# Do general badness
		for pattern in bad:
			tag=pattern[0]
			word=pattern[1]
			lemma=pattern[2]
			message=pattern[3]
			fullpattern = "\(("+tag+") ("+word+")-("+lemma+")\)"

			if re.search(fullpattern,line):
				sentence_report+="-----\n"
				sentence_report+=sentenceID+"\n"
				display_line = re.sub(fullpattern,'\033[1m'+'\033[91m'+"(\\1 \\2-\\3)"+'\033[0m',line)
				sentence_report+="LINE "+str(line_local)+": " + display_line + "\n"
				sentence_report+="MSG: "+message+"\n"
				sentence_report+="-----\n"
		# General badness done

		# Do require tag
		for pattern in req_tag:
			tag=pattern[0]
			word=pattern[1]
			lemma=pattern[2]
			message=pattern[3]
			fullpattern = "\(([\S-]+) ("+word+")-("+lemma+")\)"

			if re.search(fullpattern,line):
				corpustag=re.search(fullpattern,line).group(1)
				corpusword=re.search(fullpattern,line).group(2)
				corpuslemma=re.search(fullpattern,line).group(3)				

				if not re.match(tag,corpustag):
					sentence_report+="-----\n"
					sentence_report+=sentenceID+"\n"
					display_line = re.sub(fullpattern,'\033[1m'+'\033[91m'+"("+corpustag+" "+corpusword+"-"+corpuslemma+")"+'\033[0m',line)
					sentence_report+="LINE "+str(line_local)+": " + display_line + "\n"
					sentence_report+="MSG: "+message+"\n"
					sentence_report+="-----\n"


		# Require tag done

		# Do require lemma
		for pattern in req_lemma:
			tag=pattern[0]
			word=pattern[1]
			lemma=pattern[2]
			message=pattern[3]
			fullpattern = "\(("+tag+") ("+word+")-("+anything+")\)"

			if re.search(fullpattern,line):
				corpustag=re.search(fullpattern,line).group(1)
				corpusword=re.search(fullpattern,line).group(2)
				corpuslemma=re.search(fullpattern,line).group(3)				

				if not re.match(lemma,corpuslemma):
					sentence_report+="-----\n"
					sentence_report+=sentenceID+"\n"
					display_line = re.sub(fullpattern,'\033[1m'+'\033[91m'+"("+corpustag+" "+corpusword+"-"+corpuslemma+")"+'\033[0m',line)
					sentence_report+="LINE "+str(line_local)+": " + display_line + "\n"
					sentence_report+="MSG: "+message+"\n"
					sentence_report+="-----\n"

		# Require lemma done

		# Check for proper names
		fullpattern = "\((N|NS\-[NADG]) ("+anything+")-("+anything+")\)"
		if re.search(fullpattern,line):
			corpustag=re.search(fullpattern,line).group(1)
			corpusword=re.search(fullpattern,line).group(2)
			corpuslemma=re.search(fullpattern,line).group(3)
			if re.search("[A-ZÞÆÖÍÁÚÓÉ][\sþæðöÞÆÐÖáéýúíó]+",corpusword):
				print(corpusword)
				sentence_report+="-----\n"
				sentence_report+=sentenceID+"\n"
				display_line = re.sub(fullpattern,'\033[1m'+'\033[91m'+"("+corpustag+" "+corpusword+"-"+corpuslemma+")"+'\033[0m',line)
				sentence_report+="LINE "+str(line_local)+": " + display_line + "\n"
				sentence_report+="MSG: Non-first terminal element is capitalized. Should this be a proper name tag?\n"
				sentence_report+="-----\n"

	if len(sentence_report) > 0:
		print( sentence_report )

# Here the script starts running
f = open(sys.argv[1], 'r')
lines = f.readlines()
# print(len(lines))

currentSentence=""
displaySentence=""
line_number=0
last_line_number=1
for line in lines:
	line_number+=1
	theLine = line.strip()
	currentSentence = currentSentence + theLine + "\n"
	displaySentence = displaySentence + line
	if len(line.strip())==0:
	    process_sentence(currentSentence,last_line_number)
	    last_line_number=line_number
	    #if re.search(query,stripped.lower()):
	    #	print(re.sub(query,'\033[1m'+'\033[91m'+query+'\033[0m',stripped.lower()))
	    #	print(displaySentence)

	    currentSentence=""
	    displaySentence=""

