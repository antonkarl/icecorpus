node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms {1}[1]VB|DO|RD|BE|HV)
   AND (IP* iDoms [2]VB|DO|RD|BE|HV)

add_leaf_before{1}: (CODE *ZZZ_NO_IP_INF*)