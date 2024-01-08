#!/usr/bin/python3
#
#  ./dat2txt filepattern output_directory
#  Example: ./dat2txt.py txt/
#
import glob
import sys
import os

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
    if is_id(label):
        return True
    
    return False

def extract_text( infile_path, output_directory="./" ):
    infile = open( infile_path, "r" )
    lines = infile.readlines()    
    output=""
    for line in lines:
        chunks = line.split("\t")
        type = int(chunks[6])
        parent = int(chunks[8])
        text = chunks[9].strip()
        if( type == 3 and not is_empty(text) ):
            output += text + " "
            
        if( parent == -1 ):
            output = output.strip()+"\n"                
    output = output.replace("$ $", "")
        
    basename = os.path.basename( infile_path )  
    basename = basename[0:-8]  
    outfile = open( output_directory + basename + ".txt", "w" )     
    outfile.write( output.strip() )

file_matcher = sys.argv[1]  # like something/*.dat

output_directory = "./"

if len(sys.argv) > 2:
    output_directory = sys.argv[2]  # like data/

allfiles = glob.glob( file_matcher )
for file in allfiles:
    print( file )
    extract_text( file, output_directory )

print( "done" )



    