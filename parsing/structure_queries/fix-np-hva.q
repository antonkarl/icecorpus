copy_corpus:t

node: IP*
query: (IP* idoms {1}NP*) AND (NP* idoms {2}PRO*) AND (PRO* idoms [Hh]va*|[Hh]ver*) AND (NP* iprecedes {3}.*) AND (NP* hassister .*) AND (NP* iprecedes !C)

replace_label{1}: WNP
replace_label{2}: WPRO-CASE
add_internal_node{1, 3}: CP-XXX
add_internal_node{3, 3}: IP-SUB
add_leaf_after{1}: (C 0)