# This Python file uses the following encoding: utf-8

import sys,re,os

textname=sys.argv[1]

# Open input file for reading
f = open(textname+".txt", "r")
linelist = f.readlines()
output = ''
i=0
textId=1
for line in linelist:
	output = output + line
	i+=1
	if i%25 == 0:
		extra=""
		if textId<10:
			extra="0"
		f = open(textname+extra+str(textId)+'.txt', 'w')
		f.write(output)
		f.close()
		textId+=1
		output=''

# Last file
f = open(textname+extra+str(textId)+'.txt', 'w')
f.write(output)
f.close()

