copy_corpus:t

node: IP*
query: (IP* idoms {1}ADVP*) AND (ADVP* idoms {2}ADV*) AND (ADV* idoms [Hh]v*) AND (ADVP* iprecedes {3}.*) AND (ADVP* hassister .*) AND (ADVP* iprecedes !C) AND (ADVP* iprecedes !*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

replace_label{1}: WADVP
replace_label{2}: WADV
add_internal_node{3, 3}: IP-SUB