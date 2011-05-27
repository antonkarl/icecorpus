node: $ROOT

copy_corpus: t

query: ({1}ADVP* idoms ADV) AND (ADVP* idoms RP)

add_leaf_before{1}: (CODE *ZZZ_BAD_ADVP_PROBABLY_PP*)
