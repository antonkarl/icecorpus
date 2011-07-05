#!/usr/bin/python3
#
#  ./extract filepattern output_directory
#  Example: ./dat2txt.py txt/
#
import glob
import sys
import os

import re 

def is_id( label ):
    # horrible, but works
    return len( label.split(".") ) == 4  and len( label.split(",") ) == 2 


def is_empty( label ):
    if len(label)==0:
        return True    
    if label[0] == "*":
        return True
    if label[0] == "0":
        return True
    if label[0] == "{":
        return True
    if label[0] == "<":
        return True
    #if is_id(label):
    #    return True
    
    return False


#file = open("/home/anton/icecorpus/finished/11xx.firstgrammar.sci-lin.psd")
#lines = file.readlines()

tagword = r"\(([^ \t\n\r\(\)]+) ([^ \t\n\r\(\)]+)\)"
#allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\-'
#tagword = r'\((['+allchars+']+) (['+allchars+']+)\)'

lemmata = {}

prelemmatized = 0
lemmatized = 0
bad = 0
remaining = 0


def extract_text( infile_path, output_directory, unknowns ):
    global prelemmatized
    global lemmatized
    global bad
    global remaining
    
    infile = open( infile_path, "r" )
    alltext = infile.read()    
    output=""
    trees = alltext.split("\n\n")
    for tree in trees:        
        lines = tree.split("\n")
        for line in lines:    
            if re.search(tagword,line) != None:
                
                matches = re.findall( tagword, line )
                #print( matches )
                for match in matches:
                    tag = match[0]
                    word = match[1]
                    lemma = "0"                                
                    chunks = word.split("-")
                    if len(chunks) == 2:
                        lemma = chunks[1]
                        word = chunks[0]
                        prelemmatized += 1
                    elif len(chunks) == 1 and not is_empty( chunks[0] ) and not tag == "CODE":
                        identity = word.lower()+"_"+tag                                                
                        if identity in lemmata.keys():
                            line = line.replace(tag + " " + chunks[0], tag + " " + chunks[0]+"-"+lemmata[word.lower()+"_"+tag] )
                            lemmatized += 1
                        else:
                            remaining += 1
                            unknowns.append( chunks[0] + "\t" + tag + "\t" + chunks[0].replace("$","")  )
                    else:
                        if not is_empty( chunks[0] ) and not tag == "CODE":
                            print( word + "-" + tag + "-" +lemma)
                            bad += 1                                                    
                        
                    word = word.replace("<dash/>","-")
                                                    
                    #if not is_empty( word ) and tag != "ID" and tag!="CODE":                    
                    #    output += word + "\t" + tag + "\t"  + lemma + "\n"            
                        
            output += line + "\n"
        output += "\n"
        

    #output = output.replace("$ $", "")    
    basename = os.path.basename( infile_path )  
    basename = basename[0:-4]  
    outfile = open( output_directory + basename + ".psd", "w" )     
    outfile.write( output.strip() + "\n\n" )
        
    #for idx, value in enumerate(lemmata):
    #    print( str(idx) + "\t" + value + " "+ lemmata[value] )
            

# get input params
file_matcher = sys.argv[1]  # like something/*.dat
output_directory = sys.argv[2]  # like data/
lemmadict = sys.argv[3]
unfile = sys.argv[4] # file to put unknowns

# load lemmata
lemmafile = open(lemmadict, "r")
lines = lemmafile.readlines()
for line in lines:
    if ( len( line.split("\t") ) == 3 ):
        word, tag, lemma = line.split("\t")
        lemmata[ word.lower()+"_"+tag ] = lemma.lower().strip()

# start correcting lemmata
unknowns = []
allfiles = glob.glob( file_matcher )
for file in allfiles:
    print( file )
    extract_text( file, output_directory, unknowns )

print("prelemmatized: " +str(prelemmatized) )
print("lemmatized: " +str(lemmatized) )
print("remaining: " +str(remaining) )
print("bad: " +str(bad) )

unoutput = ""
for unknown in unknowns:
    unoutput += unknown + "\n"
open(unfile,"w").write(unoutput)

print( "done" )
