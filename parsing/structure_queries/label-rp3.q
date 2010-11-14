copy_corpus:t

node: IP*
query: ({1}PP idomstotal 2) AND (PP idoms {2}P) AND (PP idoms {3}NP) AND (P idoms út-*|upp-*|inn-*|niður-*|fram-*)

delete_node{1}:
replace_label{2}: RP
replace_label{3}: NP-OB1