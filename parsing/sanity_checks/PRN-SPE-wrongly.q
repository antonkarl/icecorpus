node: $ROOT

copy_corpus: t

query: ({1}*PRN*SPE*|*SBJ*SPE* exists)

add_leaf_before{1}: (CODE *ZZZ_SPE_PRN_OR_SPE_SBJ*)
