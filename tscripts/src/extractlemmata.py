import re
import glob 

file = open("1200.sturltest.nar-sag.psd")
lines = file.readlines()

tagword = r"\(([^ \t\n\r\(\)]+) ([^ \t\n\r\(\)]+)\)"
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\-'
tagword = r'\((['+allchars+']+) (['+allchars+']+)\)'

lemmata = {}

for line in lines:    
    if re.search(tagword,line) != None:
        tag = re.search(tagword,line).group(1)
        word = re.search(tagword,line).group(2)

        #print( tag + " " + word)

        chunks = word.split("-")
        if len(chunks) == 2:
            lemma = chunks[1]
            word = chunks[0]                
            identity = tag + "_" + word
            #print(identity)
            #if not identity in lemmata.keys():            
            lemmata[identity] = lemma


for idx, value in enumerate(lemmata):
    print( str(idx) + "\t" + value + " "+ lemmata[value] )