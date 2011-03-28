# This Python file uses the following encoding: utf-8

import sys,re

# String replacements
# Conjunctions
reps = {}
reps['(CP (C og-og))']='(CONJ og-og)'
reps['(CP (C en-en))']='(CONJ en-en)'
reps['(CP (C eða-eða))']='(CONJ eða-eða)'
reps['(CP (C eður-eður))']='(CONJ eður-eður)'
reps['(CP (C ellegar-ellegar))']='(CONJ ellegar-ellegar)'
reps['(CP (C heldur-heldur))']='(CONJ heldur-heldur)'
reps['(CP (C enda-enda))']='(CONJ enda-enda)'

# NEG 	negation, for ekki, eigi, ei

# Tag Replacements
tagreps = {}
tagreps['AP']='ADJP'
tagreps['APs ']='APS'
tagreps['AdvP ']='ADVP'


# Open input file for reading
f = open(sys.argv[1], 'r')
output = f.read()

# Do String replacements
for before,after in reps.items():
	output = output.replace(before,after)

# Do tag replacements
for before,after in tagreps.items()
	beforestring = '('+before+' '
	afterstring = '('+after+' '
	output = output.replace(before,after)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
