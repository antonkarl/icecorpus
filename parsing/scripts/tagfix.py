# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ\.$'

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read();

####### FIRST REPLACE LOOP (stuff that must be done before second loop)
# make stuff uppercase for consistency
reps = {}

reps["\(P-[ADG] "]="(P "
reps["\(VPs"]="(VPS"
reps["\(VPb"]="(VPB"
reps["\(VPg"]="(VPG"
reps["\(VPp"]="(VPP"
reps["\(VPi"]="(VPI"
reps["\(AdvP"]="(ADVP"
reps["\(AP"]="(ADJP"  # adjective phrase
reps["\(ADJPs"]="(ADJP"  # conjoined APS, modified by subsequent CS query
reps["\(NP-PRD-QUAL"]="(NP-POS"
reps["\(NP-QUAL"]="(NP-POS"
reps["\(NP-OBJ"]="(NP-OB1"
reps["\(NP-IOBJ"]="(NP-OB2"
reps["\(SCP"]="(CP-ADV"
reps["\(ADV líka-líka\)"]="(ALSO líka-líka)"
reps["\(ADVP \(ADV aðeins-aðeins\)\)"]="(FP aðeins-aðeins)"
reps["\(C þótt-þótt\)"]="(P þótt-þótt)"



reps["NP-TIMEX"]="NP"

reps["\(InjP \(ADV-I (["+allchars+"]+)-(["+allchars+"]+)\)\)"]="(INTJ \\1-\\2)"



#(MWE_CP (ADV eins-eins) (C og-og))


# ( (IP-MAT (InjP (ADV-I Ónei-ónei))

# (CP-REL (C sem-sem))
#reps["\(CP-REL (C ))"]="(CP-ADV"
#(WNP-3 0)

reps["\(MWE_AdvP"]="(ADVP-MWE"
# Make sure that all token final punctuation is a period
reps["\([,;\.:?!] ([,;\.:?!]-[,;\.:?!][\)]+\n\n)"]="(. \\1"

for before,after in reps.items():	
	output = re.sub(before, after, output)

####### SECOND REPLACE LOOP

reps = {}
reps["\(ADV aðeins-aðeins\)"]="(FP aðeins-aðeins)"
# Some basic structures
# reps["\(CP-ADV \(C (sem|er)-\\1\)\)"]="(CP-REL (WNP-X 0) (C \\1-\\1))"

# NOUNS 

# NPR 	proper noun, singular
# NPRS 	proper noun, plural
# NS 	common noun, plural
reps["\(N-([A-Z]S[A-Z]{2}[PLO])"]="(NPR-\\1" # proper noun, singular
reps["\(N-([A-Z]P[A-Z]{2}[C])"]="(NS-\\1" # common noun, plural
reps["\(N-([A-Z]P[A-Z]{2}[PLO])"]="(NPRS-\\1" # proper noun, plural

# Do possesives using CorpusSearch queries because structure based
# must use NP-QUAL also, all genitives is too much, cf. til-genitives 
# reps["N$"]="(N)-([A-Z]SG[A-Z]{2})" # common noun, singular, possessive

# ADJECTIVES


reps["\(ADJ-([A-Z]{4}C)"]="(ADJR-\\1" # adjective, comparative
reps["\(ADJ-([A-Z]{4}S)"]="(ADJS-\\1" # adjective, superlative

# VERBS
reps["\(V-(D[A-Z]{4})"]="(VAN-\\1" # VAN, passive participle (verbal or adjectival)
reps["\(V-(P[A-Z123])"]="(VAG-\\1" # VAN, present participle
reps["\(V-T[AM]"]="(VB" # VB, infinitive
reps["\(V-(M[A-Z123]+)"]="(VBI-\\1"  # VBI, imperative
reps["\(V-([IS][A-Z][123][A-Z]D)"]="(VBD-\\1"  # VBD, past (including past subjunctive)
reps["\(V-([IS][A-Z][123][A-Z]P)"]="(VBP-\\1"  # VBP, present (including present subjunctive)
reps["\(V-(U[AM])"]="(VBN-\\1"  # VBN, perfect participle

# Verb Phrase, infinitive > IP-INF
reps["\(VPI"]="(IP-INF"

# QUANTIFIERS 
# báðir, allir, nokkrir, sumir, einhverjir, fáir, fáeinir, enginn
reps["\(PRO-(X[A-Z]{3}) (["+allchars+"]+)-(allur|báðir|nokkur|enginn|sumur|fáeinir|fár|einhver)\)"]="(Q-\\1 \\2-\\3)"

#(ADJ-N margur-margur)

# Infinitival að
reps["\(C-I að-að\)"]="(TO að-að)"

# C-R
reps["\(C-R "]="(C "

# ADVERBS
reps["\(ADV-NC (["+allchars+"]+)-(["+allchars+"]+)\)"]="(ADVR \\1-\\2)" # ADVC
reps["\(ADV-NS (["+allchars+"]+)-(["+allchars+"]+)\)"]="(ADVS \\1-\\2)" # ADVS

# ONE 	the word ONE (except as focus particle) 
reps['\(NUM-([A-Z]{4} ['+allchars+']+-einn)\)']="(ONE-\\1)"

# NEGATION
reps['\(ADVP \(ADV ([Ee]kki|[Ee]igi|[Ee]i)-(ekki|eigi|ei)\)\)']='(NEG \\1-\\2)'

# CONJUNCTIONS
reps['\(CP \(C ([Oo]g|[Ee]n|[Ee]ða|[Ee]llegar|[Hh]eldur|[Ee]nda)-([Oo]g|[Ee]n|[Ee]ða|[Ee]llegar|[Hh]eldur|[Ee]nda)\)\)']='(CONJ \\1-\\2)'


reps["\(CP-ADV \(C bæði-bæði\)\)"]="(CONJ bæði-bæði)"

for before,after in reps.items():	
	output = re.sub(before, after, output)


##### THIRD REPLACE LOOP
# based on stuff that happened in previous loops

reps={}

#VERA (BE)
reps["\(VB (["+allchars+"]+)-vera\)"]="(BE \\1-vera)"  # BE 	BE, infinitive
reps["\(VAG-[A-Z123]{2} ([Vv]erandi)-vera\)"]="(BAG \\1-vera)"  # BAG 	BE, present participle
reps["\(VBI-[A-Z123]{5} (["+allchars+"$]+)-vera\)"]="(BEI \\1-vera)"  # BEI 	BE, imperative
reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-vera\)"]="(BED\\1 \\2-vera)"  # BED 	BE, past (including past subjunctive)
reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-vera\)"]="(BEP\\1 \\2-vera)"  # BEI 	BE, present (including present subjunctive)
reps["\(VBN-[A-Z123]{2} (["+allchars+"]+)-vera\)"]="(BEN \\1-vera)"  # BEN 	BE, perfect participle
# BEN 	BE, perfect participle

# HAFA (HAVE)
reps["\(VB hafa-hafa\)"]="(HV hafa-hafa)"  #HV 	HAVE, infinitive
reps["\(VAG-[A-Z123]{2} ([Hh]afandi)-hafa\)"]="(HAG \\1-hafa)"   #HAG 	HAVE, present participle
reps["\(VBI-[A-Z123]{5} (["+allchars+"$]+)-hafa\)"]="(HVI \\1-hafa)"  #HVI 	HAVE, imperative
reps["\(VAN-[A-Z123]{5} (["+allchars+"]+)-hafa\)"]="(HAN \\1-hafa)" #HAN 	HAVE, passive participle (verbal or adjectival)
reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-hafa\)"]="(HVD\\1 \\2-hafa)"  #HVD 	HAVE, past (including past subjunctive)
reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-hafa\)"]="(HVP\\1 \\2-hafa)"  #HVP 	HAVE, present (including present subjunctive) 
reps["\(VBN-[A-Z123]{2} (["+allchars+"]+)-hafa\)"]="(HVN \\1-hafa)"  # HVN

# GERA (DO)
reps["\(VB ([Gg]era|gjöra)-(gera|gjöra)\)"]="(DO \\1-gera)"  #DO 	DO, infinitive
reps["\(VAG-[A-Z123]{2} ([Gg]erandi|gjörandi)-(gera|gjöra)\)"]="(DAG \\1-gera)"  
reps["\(VBI-[A-Z123]{5} (["+allchars+"$]+)-(gera|gjöra)\)"]="(DOI \\1-gera)"  
reps["\(VAN-[A-Z123]{5} (["+allchars+"]+)-(gera|gjöra)\)"]="(DAN \\1-gera)"
reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-(gera|gjöra)\)"]="(DOD\\1 \\2-gera)"  
reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-(gera|gjöra)\)"]="(DOP\\1 \\2-gera)"
reps["\(VBN-[A-Z123]{2} (["+allchars+"]+)-(gera|gjöra)\)"]="(DON \\1-gera)" 


# VERÐA (WERDEN)
reps["\(VB ([Vv]erða)-verða\)"]="(RD \\1-verða)" 
reps["\(VAG-[A-Z123]{2} [Vv]erðandi-verða\)"]="(RAG verðandi-verða)"  
reps["\(VBI-[A-Z123]{5} (["+allchars+"$]+)-verða\)"]="(RDI \\1-verða)" 
reps["\(VAN-[A-Z123]{5} (["+allchars+"]+)-verða\)"]="(RAN \\1-verða)" 
reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-verða\)"]="(RDD\\1 \\2-verða)"  
reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-verða\)"]="(RDP\\1 \\2-verða)"  
reps["\(VBN-[A-Z123]{2} (["+allchars+"]+)-verða\)"]="(RDN \\1-verða)" 

# MODALS
modal = "skulu|munu|mega|vilja|geta"

reps["\(VB ("+modal+")-("+modal+")\)"]="(MD \\1-\\2)"  
#reps["\(VAN-[A-Z123]{5} (["+allchars+"]+)-("+modal+")\)"]="(MAN \\1-\\2)"
#reps["\(VBI-[A-Z123]{5} (["+allchars+"$]+)-("+modal+")\)"]="(MDI \\1-gera)"  
reps["\(VBD-([IS])[A-Z123]{4} (["+allchars+"]+)-("+modal+")\)"]="(MDD\\1 \\2-\\3)"  
reps["\(VBP-([IS])[A-Z123]{4} (["+allchars+"]+)-("+modal+")\)"]="(MDP\\1 \\2-\\3)"
# reps["\(VBN-[A-Z123]{2} (["+allchars+"]+)-("+modal+")\)"]="(MDN \\1-\\2)" 


for before,after in reps.items():	
	output = re.sub(before, after, output)

###### FORTH REPLACE LOOP
reps={}

# REDUCE TAGS
# (VPP (VAN-DANSN sprottið-spretta))
# reps["\(VPP \(VAN-D[A-Z123]{4} ["+allchars+"]-["+allchars+"]\)\)"]="(VAN)"

# Preserve only case information in extended tag for nouns
reps["\((N|NPR|NS|NPRS)-[A-Z]{2}([A-Z])[A-Z]{2} (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1-\\2 \\3)"

# Preserve only the predashial ADJ for adjectives, plus case
reps["\((ADJ|ADJR|ADJS)-[A-Z]{2}([NADGX])[A-Z]{2} (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1-\\2 \\3)"

# Preserve only the predashial ADV for adverbs 
reps["\((ADV|ADVR|ADVS)-[A-Z]{2} (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1 \\2)"
reps["\(ADV-W (["+allchars+"]+-["+allchars+"]+)\)"]="(WADV \\1)"

# Preserve the indicative vs. subjunctive distinction on verbs
# XXXXX
reps["\((VBP|VBD|BED|BEP|HVD|HVP|MDP|MDD)-([IS])[A-Z123]{4} (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1\\2 \\3)"

# Preserve only predashial tag on imperative verbs
reps["\(VBI-[A-Z123]+ "]="(VBI "

# Preserve only predashial tag on infinitive verbs
# disappears earlier
# reps["\((VB|HV|BE)-[A-Z]{2} (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1 \\2)"
#	  (VPB (HV-TA hafa-hafa))

# Preserve only case information on PRO and stuff that has the same kind of an extended tag
reps["\((ONE|NUM|PRO|D|Q)-[A-Z123]{3}([NADG]) (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1-\\2 \\3)"
#(ONE-PNSN eitt-einn)

# Preserve only the predashial tag on participles
reps["\((VAN|VAG|VBN)-([A-Z]{2}|[A-Z]{5}) (["+allchars+"]+-["+allchars+"]+)\)"]="(\\1 \\3)"

# Preserve only predashial stuff on numbers
#	  (NP-POS (NUM-PNPG sextán-sextán) (NS-G vetra-vetur))

for before,after in reps.items():	
	output = re.sub(before, after, output)


###### FIFTH LOOP
reps={}
reps["\(VPP (\((VAN|HAN) ["+allchars+"]+-["+allchars+"]+\))\)"]="\\1"
reps["\(VPS (\((VBN|BEN) ["+allchars+"]+-["+allchars+"]+\))\)"]="\\1"

reps["\(VPB \(TO að-að\) \(BE vera-vera\)\)"]="(IP-INF (TO að-að) (BE vera-vera))"
reps["\(VPB \(BE vera-vera\)\)"]="(BE vera-vera)"


reps["\(PRO-([NADG]) (["+allchars+"]+-sá)\)"]="(D-\\1 \\2)"
reps["\(PRO-([NADG]) (["+allchars+"]+-þessi)\)"]="(D-\\1 \\2)"
#	  (NP-OB1 (D-A það-sá))

reps["\(PRO-([NADG] ["+allchars+"]+-annar)\)"]="(OTHER-\\1)"


#MWE fixes
reps["\(MWE_CP \(ADV eins-eins\) \(C og-og\)\)"]="(ADJP (ADVR eins) (PP (P og)))"
reps["\(MWE_PP \(ADV niðri-niðri\) \(P í-í\)\)"]="(ADV niðri-niðri) (P í-í)"
reps["\(PP \(MWE_PP \(ADV út-út\) \(P í-í\)\)"]="(PP (RP út-út) (P í-í)"


reps["\(MWE_CP \(P til-til\) \(TO að-að\)\)"]="(PP (P til-til) (TO að-að))"
reps["\(MWE_CP \(P til-til\) \(PRO-G þess-það\)\)"]="(PP (P til-til) (PRO-G þess-það))"

reps["\(MWE_CP \(P til-til\) \(PRO-G þess-það\) \(TO að-að\)\)"]="(PP (P til-til) (NP (PRO-G þess-það)) (IP-INF-PRP (C að-að)))"
# reps["\(CP \(P til-til\) \(PRO-G þess-það\) \(TO að-að\)\)"]="(PP (P til-til) (NP (PRO-G þess-það)) (IP-INF-PRP (C að-að)))"
      #(CP (P til-til) (PRO-G þess-það) (TO að-að))

reps["\(ADVP-MWE \(PRO-D einu-einn\) \(N-D sinni-sinn\)\)"]="(NP-TMP (ONE-D einu-einn) (N-D sinni-sinn))"

reps["\(MWE_CP \(PRO-D því-það\) \(C að-að\)\)"]="(PP (P því-því) (C að-að))"

reps["\(MWE_CP \(P af-af\) \(PRO-D því-það\) \(C að-að\)\)"]="(PP (P af-af) (PRO-D því-það) (CP-THT (C að-að)))"

reps["\(MWE_PP \(ADV aftur-aftur\) \(P í-í\)\)"]="(ADV aftur-aftur) (P í-í)"

reps["\(ADVP-MWE \(Q-A einhvern-einhver\) \(N-A veg\$-vegur\) \(D-A \$inn-hinn\)\)"]="(NP-ADV (Q-A einhvern-einhver) (N-A veg$-vegur) (D-A $inn-hinn))"

reps["\(ADVP-MWE \(OTHER-G annars-annar\) \(N-G staðar-staður\)\)"]="(NP-ADV (NP-POS (OTHER-G annars-annar)) (N-G staðar-staður))"

reps["\(ADVP-MWE \(C hvort-hvort\) \(C sem-sem\)\)"]="(CP-QUE (WQ hvort-hvort) (C sem-sem))"

reps["\(ADVP-MWE \(P um-um\) \(N-A leið-leið\)\)"]="(PP (P um-um) (NP (N-A leið-leið)))"

reps["\(ADVP \(ADV þó-þó\) \(ADV "]="(ADVP (ADV þó-þó)) (ADVP (ADV "

reps["\(PP \(MWE_PP \(ADV á-á\) \(P móti-móti\)\)"]="(PP (P á-á) (NP (N-D móti-móti))"


reps["\(ADVP-MWE \(P á-á\) \(PRO-A hinn-hinn\) \(N-A bóg\$-bógur\) \(D-A \$inn-hinn\)\)"]="(PP (P á-á) (NP (D-A hinn-hinn) (N-A bóg$-bógur) (D-A $inn-hinn)))"

reps["\(ADVP-MWE \(P að-að\) \(ADJS-D minnsta-lítill\) \(N-D kosti-kostur\)\)"]="(PP (P að-að) (NP (ADJS-D minnsta-lítill) (N-D kosti-kostur)))"

reps["\(MWE_CP \(ADV svo-svo\) \(C að-að\)\)"]="(ADVP (ADVR svo-svo) (C að-að))"

reps["\(MWE_CP \(ADV áður-áður\) \(C en-en\)\)"]="(ADVP-TMP (ADVR áður-áður) (PP (P en-en) (CP-CMP (WADVP 0))))"

reps["\(MWE_AP \(PRO-G þess-það\) \(N-G háttar-háttur\)\)"]="(NP-POS (PRO-G þess-það) (N-G háttar-háttur))"

reps["\((NS|PRO)-[NADG] ((hvorirtv|hvortv|hvorttv)[a-z]+)-([a-z]+)\)"]="(Q+NUM \\2-hvortveggja)"
#"(NS-G hvorirtveggja-hvorirtveggur)"

reps["\(ADVP \(ADV einnig-einnig\)\)"]="(ALSO einnig-einnig)"

reps["\(ADV ekki-ekki\)"]="(NEG ekki-ekki)"

reps["\(ADVP \(ADV hvernig-hvernig\)\)"]="(CP-QUE (WADVP (WADV hvernig-hvernig)))"

reps["\(ADJP \(ADJ-([NADG]) (marg[a-z]+)-margur\)\)"]="(Q-\\1 \\2-margur)"
reps["\(ADJP \(ADJR-([NADG]) (fleir[a-z]+)-margur\)\)"]="(QR-\\1 \\2-margur)"
reps["\(ADJP \(ADJS-([NADG]) (flest[a-z]+)-margur\)\)"]="(QS-\\1 \\2-margur)"

reps["\(ADJP \(ADJ-([NADG]) (miki[a-z]+)-mikill\)\)"]="(Q-\\1 \\2-mikill)"
reps["\(ADJP \(ADJR-([NADG]) (meir[a-z]+)-mikill\)\)"]="(QR-\\1 \\2-mikill)"
reps["\(ADJP \(ADJS-([NADG]) (mest[a-z]+)-mikill\)\)"]="(QS-\\1 \\2-mikill)"

reps["\(PRO-([NADG]) (["+allchars+"]+)-slíkur\)"]="(SUCH-\\1 \\2-slíkur)"

# (PRO-N slíkt-slíkur)

for before,after in reps.items():	
	output = re.sub(before, after, output)


###### SIXTH LOOP, some more structure and stuff
reps={}

reps["\(ADJ-([NADG]) (marg[a-z]+)-margur\)"]="(Q-\\1 \\2-margur)"
reps["\(ADJR-([NADG]) (fleir[a-z]+)-margur\)"]="(QR-\\1 \\2-margur)"
reps["\(ADJS-([NADG]) (flest[a-z]+)-margur\)"]="(QS-\\1 \\2-margur)"

reps["\(ADJ-([NADG]) (miki[a-zð]+)-mikill\)"]="(Q-\\1 \\2-mikill)"
reps["\(ADJR-([NADG]) (meir[a-z]+)-mikill\)"]="(QR-\\1 \\2-mikill)"
reps["\(ADJS-([NADG]) (mest[a-z]+)-mikill\)"]="(QS-\\1 \\2-mikill)"


reps["MWE_"]=""
reps["-MWE"]=""

reps["\(CP-ADV \(C (sem|er)-\\1\)\)"]="(CP-REL (WNP 0) (C \\1-\\1))"
reps["\(CP-ADV \(C ([Aa]ð)-að\)\)"]="(CP-THT (C \\1-að))"

for before,after in reps.items():	
	output = re.sub(before, after, output)



# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()





