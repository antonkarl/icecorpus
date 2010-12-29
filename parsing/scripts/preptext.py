import sys
import re

f = open(sys.argv[1], 'r')
currentText = f.read()

currentText = re.sub("\|k([0-9]+)","(COM:chapter\\1)",currentText)
currentText = re.sub("\|s([0-9]+)","(P:\\1)",currentText)

currentText = re.sub("\.\n",". ",currentText)
currentText = re.sub("\n"," ",currentText)
currentText = re.sub("[ ]+"," ",currentText)
currentText = re.sub("([\.\?][\"]{0,1}) ([A-ZÞÆÖÓÁÉÚÍ\"\'\(])","\\1\n\\2",currentText)
currentText = re.sub("\.\nKapituli.",". Kapituli.",currentText)

currentText = currentText.strip()

print(currentText)
