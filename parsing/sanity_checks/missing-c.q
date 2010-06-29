node: $ROOT

copy_corpus: t

query: ($ROOT doms {1}CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF* idoms IP-SUB*) AND (CP-CMP*|CP-THT*|CP-QUE|CP-DEG*|CP-REL*|CP-CAR*|CP-FRL*|CP-CLF* idoms !C)

append_label{1}: -ZZZ-MISS_C
