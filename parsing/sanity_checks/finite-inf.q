node: IP*|$ROOT

define: def/ICE.def

copy_corpus: t

query: (IP-INF* iDoms {1}finiteVerb)

add_leaf_before{1}: (CODE *ZZZ_SHOULD_BE_INF*)