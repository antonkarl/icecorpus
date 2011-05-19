copy_corpus: t

node: $ROOT 	
query: ({1}V* iDoms !*a|*st|*sjá|\*|V*|*-fá|*-munu|*-skulu|*-ske|*-gá|*-*á|*-þvo)

add_leaf_before{1}: (CODE *ZZZ_NOT_A_VERB*)
