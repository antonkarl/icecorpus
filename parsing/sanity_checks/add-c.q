node: CP*

copy_corpus: t

query: (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*|CP-ADV* idoms {1}IP-SUB*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*|CP-ADV* idoms !C)

add_leaf_before{1}: (C 0)
