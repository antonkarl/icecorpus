node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms VBD*|VBP*)
   AND (IP* iDoms {1}VB|DO|RD|BE|HV|MD)

add_leaf_before{1}: (CODE *ZZZ_NO_IP_INF*)
