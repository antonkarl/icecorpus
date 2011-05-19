node: IP*

copy_corpus: t

query: (IP* doms {1}CP-QUE|CP-QUE-SBJ) AND (CP-QUE|CP-QUE-SBJ idoms IP-SUB*) AND (CP-QUE|CP-QUE-SBJ idoms !C) AND (IP-SUB* idomsnumber 1 !VB*S|BE*S|DO*S|HV*S)

add_leaf_before{1}: (CODE *ZZZ_MISS_C*)