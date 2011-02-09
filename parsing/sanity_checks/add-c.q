node: IP*|QTP|FRAG

copy_corpus: t

query: (IP*|QTP|FRAG doms CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF* idoms {1}IP-SUB*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF* idoms !C)

add_leaf_before{1}: (C 0)
