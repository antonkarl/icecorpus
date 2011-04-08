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

def extract_text( infile_path, output_directory ):

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
                        
                    word = word.replace("<dash/>","-")
                                                    
                    if not is_empty( word ) and tag != "ID" and tag!="CODE":                    
                        output += word + "\t" + tag + "\t"  + lemma + "\n"
            
        output += "\n"
    
    output = output.replace("$ $", "")    
    basename = os.path.basename( infile_path )  
    basename = basename[0:-4]  
    outfile = open( output_directory + basename + ".tagged", "w" )     
    outfile.write( output.strip() )
        
    #for idx, value in enumerate(lemmata):
    #    print( str(idx) + "\t" + value + " "+ lemmata[value] )
            

# get input params
file_matcher = sys.argv[1]  # like something/*.dat
output_directory = sys.argv[2]  # like data/

allfiles = glob.glob( file_matcher )
for file in allfiles:
    print( file )
    extract_text( file, output_directory )

print( "done" )
