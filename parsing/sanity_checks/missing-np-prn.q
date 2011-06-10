node: $ROOT

copy_corpus: t

query: (!NP-PRN* idoms {1}PRO*) AND (PRO* idoms *-sjálfur)

add_leaf_before{1}: (CODE *ZZZ_MISS_NPPRN*)
