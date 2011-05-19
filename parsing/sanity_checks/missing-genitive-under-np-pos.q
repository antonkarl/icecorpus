node: $ROOT

copy_corpus: t

query: (NP-POS* iDoms {1}N*-N|N*-A|N*-D)

add_leaf_before{1}: (CODE *ZZZ_MISS_GENITIVE*)
