node: $ROOT

copy_corpus: t

query: (IP* idoms NP-OB1*) AND ({1}NP-OB1* idoms *-D) AND (NP-OB1* hasSister VAN|DAN|RAN|MAN|HAN)

add_leaf_before{1}: (CODE *ZZZ_probably_OB2*)
