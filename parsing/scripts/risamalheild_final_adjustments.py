# This Python file uses the following encoding: utf-8

### Makes adjustments to .ipsd files as the last step in txt2ipsd-risamalheild.sh.

### Usage:
### python3 risamalheild_fix_abbreviations.py [input file] [output file]

### Created by Kristján Rúnarsson

import sys,re

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()
f.close()

wordchars = "A-Za-z0-9ÁáÐðÉéÍíÓóÚúÝýÞþÆæÖöØøÄäÜü"

# fix dashes inside words
# word-final dash (e.g. efnahags-)
# (ADJ-N efnahags99xCOM_dashx66-efnahags99xcom_dashx66)
output = re.sub(r"\(([A-Z0-9-]+) (["+wordchars+"]+)99xCOM_dashx66-(["+wordchars+"]+)99xcom_dashx66\)", r"(\1 \2<dash/>-\3)", output)
# mid-word dash (e.g. EFTA-ríkin)
output = re.sub(r"\(([A-Z0-9-]+) (["+wordchars+"]+)99xCOM_dashx66(["+wordchars+"]+)-(["+wordchars+"]+)99xcom_dashx66(["+wordchars+"]+)\)", r"(\1 \2<dash/>\3-\4<dash/>\5)", output)
# correct lemma for common words
output = re.sub(r"\([A-Z0-9-]+ efnahags<dash/>-efnahags\)", r"(NP-POS (N-G efnahags<dash/>-efnahagur))", output)

# change (CODE {COM:dash}) to (, <dash/>)
output = output.replace("(CODE {COM:dash})", "(, <dash/>)")

# resolve common abbreviations that were already parsed as a single token (including the final dot)
output = output.replace("(as t.d.-t.d.)", "(PP (P t.$-til) (N-G $d.-dæmi))")
output = output.replace("(as þ.e.-þ.e.)", "(IP-MAT-PRN (NP-SBJ (PRO-N þ.$-það)) (BEPI $e.-vera))")
output = output.replace("(as þús.-þús.)", "(NUM-N þús.-þúsund)")
output = output.replace("(as kr.-kr.)", "(NS-N kr.-króna)")
output = output.replace("(as bls.-bls.)", "(N-D bls.-blaðsíða)")

# fix tag for some other common abbreviations
output = re.sub("\(as ([Hh])v.-háttvirtur\)", "(ADJ-N \1v.-háttvirtur)")
output = re.sub("\(as ([Hh])æstv.-hæstvirtur\)", "(ADJ-N \1v.-hæstvirtur)")
output = re.sub("\(as ([Þþ])m.-þingmaður\)", "(NPR-N \1m.-þingmaður)")

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
