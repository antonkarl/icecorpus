# This Python file uses the following encoding: utf-8

import sys,re,os

textname=sys.argv[1]
# mydir="/home/anton/localtrees/parsing/current/"+textname

# Create directories
if not os.path.isdir( 'current/'+textname + 'Segments' ):
	os.makedirs( 'current/'+textname + 'Segments' )

#if not os.path.isdir( "current/"+textname + "Ipsd/" ):
#	os.makedirs( "current/"+textname + "Ipsd/" )

#if not os.path.isdir( "current/"+textname + "Psd/" ):
#	os.makedirs( "current/"+textname + "Psd/" )

# Open input file for reading
f = open("current/"+textname+".segments", "r")
linelist = f.readlines()
output = ''
i=0
textId=1
for line in linelist:
	output = output + line
	i+=1
	if i%100 == 0:
		f = open('current/'+textname+'Segments/'+textname+str(textId)+'.segments', 'w')
		f.write(output)
		f.close()
		textId+=1
		output=''


