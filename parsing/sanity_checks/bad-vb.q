node: $ROOT

copy_corpus: t

query: (IP* idoms [1]VB*|VAN) AND ({1}[1]VB*|VAN hasSister [2]VB*|VAN)
       AND ([1]VB*|VAN hasSister !CONJ)

add_leaf_before{1}: (CODE *ZZZ_PROBABLY_NOT_VB*)
