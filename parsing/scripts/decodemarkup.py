# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()

# Decode page numbers
#(NUM-PMPN 99xP_3x66-99xp_3x66)
output = re.sub("\(NUM-[A-Z]+ 99xP_([0-9]+)x66-99xp_([0-9]+)x66\)", "(CODE <P_\\1>)", output)

# Decode MS comments
#(NUM-OIC 99xMS_fórarx66-99xms_fórarx66)
# (NP-SBJ (NUM-N 99xMS_ney_lekastax66-99xms_ney_lekastax66) (NS-N þrifnaðar-þrifnaði)) 
output = re.sub("\(NUM-[A-Z]+ 99xMS_(["+allchars+"0-9\_]+)x66-99xms_(["+allchars+"0-9\_]+)x66\)", "(CODE MS:\\1)", output)

# Decode VS comments (bible verse)
output = re.sub("\(NUM-[A-Z]+ 99xVS_(["+allchars+"0-9\_]+)x66-99xvs_(["+allchars+"0-9\_]+)x66\)", "(CODE VS:\\1)", output)

# Decode parentheses
output = re.sub("\(NUM-[A-Z]+ 99xPR_Sx66-99x(pr|PR)_sx66\)", "(CODE <paren>)", output)
output = re.sub("\(NUM-[A-Z]+ 99xPR_Ex66-99x(pr|PR)_ex66\)", "(CODE </paren>)", output)

# Decode COM comments
#(NUM-PMPA 99xCOM_Insertion_from_manuscript_B_endsx66-99xcom_insertion_from_manuscript_b_endsx66)
output = re.sub("\(NUM-[A-Z]+ 99xCOM_(["+allchars+"0-9_]+)x66-99x(com|COM)_(["+allchars+"0-9_]+)x66\)", "(CODE {COM:\\1})", output)

#output = re.sub("\(MS:(["+allchars+"0-9]+)\)", "99xMS_\\1x66", output)

#output = re.sub("\(COM:(["+allchars+"0-9_]+)\)", "99xCOM_\\1x66", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
