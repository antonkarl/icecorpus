node: IP*

copy_corpus: t

query: (PP* idoms CP-ADV*) AND (CP-ADV* idoms {1}IP-SUB*) AND (CP-ADV* idoms !C)

add_leaf_before{1}: (C 0)
