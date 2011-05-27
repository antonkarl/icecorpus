node: $ROOT

copy_corpus: t

query: ({1}\*ICH\*|\*T\* exists)

add_leaf_before{1}: (CODE *ZZZ_MISS_INDEX*)
