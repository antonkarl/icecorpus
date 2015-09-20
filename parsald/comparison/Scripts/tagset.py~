# This Python file uses the following encoding: utf-8

import sys,re

# Define RegEx patterns for Icelandic characters and sets of definite nouns
allchars = 'a-zA-ZþæðöÞÆÐÖáéýúíóÁÉÝÚÍÓ$'
enCase = {'n':'N','o':'A','þ':'D','e':'G'}

# Open input file for reading
f = open(sys.argv[1], 'r')
# linelist = f.readlines()
output = f.read()

output = re.sub("\(c ", "(C ", output)

output = re.sub("\(ct ", "(C ", output)

output = re.sub("\(cn ", "(TO ", output)

output = re.sub("\(e ", "(FW ", output)

output = re.sub("\(a[oeþ] ", "(P ", output)

#output = re.sub("\(ae ", "(P ", output)

#output = re.sub("\(aþ ", "(P ", output)

output = re.sub("\(a[aoþe] ", "(ADV ", output)

output = re.sub("\(a[aoþe]m ", "(ADVR ", output)

output = re.sub("\(a[aoþe]e ", "(ADVS ", output)

output = re.sub("\(au ", "(INTJ ", output)

output = re.sub("\(t...n ", "(NUM-N ", output)

output = re.sub("\(t...o ", "(NUM-A ", output)

output = re.sub("\(t...þ ", "(NUM-D ", output)

output = re.sub("\(t...e ", "(NUM-G ", output)

output = re.sub("\(n.en ", "(N-N ", output)

output = re.sub("\(n.eo ", "(N-A ", output)

output = re.sub("\(n.eþ ", "(N-D ", output)

output = re.sub("\(n.ee ", "(N-G ", output)

output = re.sub("\(n.fn ", "(NS-N ", output)

output = re.sub("\(n.fo ", "(NS-A ", output)

output = re.sub("\(n.fþ ", "(NS-D ", output)

output = re.sub("\(n.fe ", "(NS-G ", output)

output = re.sub("\(n.eng ", "(N-N ", output)

output = re.sub("\(n.eog ", "(N-A ", output)

output = re.sub("\(n.eþg ", "(N-D ", output)

output = re.sub("\(n.eeg ", "(N-G ", output)

output = re.sub("\(n.fng ", "(NS-N ", output)

output = re.sub("\(n.fog ", "(NS-A ", output)

output = re.sub("\(n.fþg ", "(NS-D ", output)

output = re.sub("\(n.feg ", "(NS-G ", output)

output = re.sub("\(n.en.[mös] ", "(NPR-N ", output) #proper names, e.g. ngen-m Grímur

output = re.sub("\(n.eo.[mös] ", "(NPR-N ", output)

output = re.sub("\(n.eþ.[mös] ", "(NPR-N ", output)

output = re.sub("\(n.ee.[mös] ", "(NPR-N ", output)

output = re.sub("\(n.fn.[mös] ", "(NPRS-N ", output)

output = re.sub("\(n.fo.[mös] ", "(NPRS-N ", output)

output = re.sub("\(n.fþ.[mös] ", "(NPRS-N ", output)

output = re.sub("\(n.fe.[mös] ", "(NPRS-N ", output)

output = re.sub("\(l..n.f ", "(ADJ-N ", output)

output = re.sub("\(l..o.f ", "(ADJ-A ", output)

output = re.sub("\(l..þ.f ", "(ADJ-D ", output)

output = re.sub("\(l..e.f ", "(ADJ-G ", output)

output = re.sub("\(l..n.m ", "(ADJR-N ", output)

output = re.sub("\(l..o.m ", "(ADJR-A ", output)

output = re.sub("\(l..þ.m ", "(ADJR-D ", output)

output = re.sub("\(l..e.m ", "(ADJR-G ", output)

output = re.sub("\(l..n.e ", "(ADJS-N ", output)

output = re.sub("\(l..o.e ", "(ADJS-A ", output)

output = re.sub("\(l..þ.e ", "(ADJS-D ", output)

output = re.sub("\(l..e.e ", "(ADJS-G ", output)

output = re.sub("\(fa..n ", "(D-N ", output)

output = re.sub("\(fa..o ", "(D-A ", output)

output = re.sub("\(fa..þ ", "(D-D ", output)

output = re.sub("\(fa..e ", "(D-G ", output)

output = re.sub("\(fb..n ", "(ADJ-N ", output)

output = re.sub("\(fb..o ", "(ADJ-A ", output)

output = re.sub("\(fb..þ ", "(ADJ-D ", output)

output = re.sub("\(fb..e ", "(ADJ-G ", output)

output = re.sub("\(fe..n ", "(PRO-N ", output)

output = re.sub("\(fe..o ", "(PRO-A ", output)

output = re.sub("\(fe..þ ", "(PRO-D ", output)

output = re.sub("\(fe..e ", "(PRO-G ", output)

output = re.sub("\(fo..n ", "(Q-N ", output)

output = re.sub("\(fo..o ", "(Q-A ", output)

output = re.sub("\(fo..þ ", "(Q-D ", output)

output = re.sub("\(fo..e ", "(Q-G ", output)

output = re.sub("\(fp..n ", "(PRO-N ", output)

output = re.sub("\(fp..o ", "(PRO-A ", output)

output = re.sub("\(fp..þ ", "(PRO-D ", output)

output = re.sub("\(fp..e ", "(PRO-G ", output)

output = re.sub("\(fs..n ", "(WPRO-N ", output)

output = re.sub("\(fs..o ", "(WPRO-A ", output)

output = re.sub("\(fs..þ ", "(WPRO-D ", output)

output = re.sub("\(fs..e ", "(WPRO-G ", output)

output = re.sub("\(g..n ", "(D-N ", output)

output = re.sub("\(g..o ", "(D-A ", output)

output = re.sub("\(g..þ ", "(D-D ", output)

output = re.sub("\(g..e ", "(D-G ", output)

output = re.sub("\(sn ", "(TO ", output)

output = re.sub("\(sng ", "(TO ", output)

output = re.sub("\(snm ", "(TO ", output)

output = re.sub("\(sb.... ", "(VBI ", output)

output = re.sub("\(sf...þ ", "(VBDI ", output)

output = re.sub("\(sf...n ", "(VBPI ", output)

output = re.sub("\(sv...þ ", "(VBDS ", output)

output = re.sub("\(sv...n ", "(VBPS ", output)

output = re.sub("\(ss. ", "(VBN ", output)

output = re.sub("\(sl. ", "(VAG ", output)

output = re.sub("\(sþ.... ", "(VAN ", output)

# Write result to output file
f = open(sys.argv[2], 'w')
f.write(output)
f.close()
