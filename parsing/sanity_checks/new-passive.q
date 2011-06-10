node: $ROOT

copy_corpus: t

query: (VAN* hasSister NP-OB*) AND ({1}NP-OB* idoms *-A)

add_leaf_before{1}: (CODE *ZZZ_NEW_PASSIVE*)
