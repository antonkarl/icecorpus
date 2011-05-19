node: CP*

copy_corpus: t

query: ({1}CP-CMP*|CP-THT*|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*|CP-ADV* idoms IP-SUB*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*|CP-ADV* idoms !C) AND (IP-SUB* idomsnumber 1 !VB*S|BE*S|DO*S|HV*S)

add_leaf_before{1}: (CODE *ZZZ_MISS_C*)
