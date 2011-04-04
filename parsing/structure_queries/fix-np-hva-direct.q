copy_corpus:t

node: IP*
query: (IP* idoms {1}NP*) AND (NP* idoms {2}PRO*) AND (PRO* idoms [Hh]va*|[Hh]ver*) AND (NP* iprecedes {3}.*) AND (NP* hassister .*) AND (NP* iprecedes !C) AND (NP* iprecedes *MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

replace_label{1}: WNP
replace_label{2}: WPRO-N
add_internal_node{3, 3}: IP-SUB
