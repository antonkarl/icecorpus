node: IP*

copy_corpus: t

query: (IP-INF* iDoms NP-OB*)
   AND (IP* idoms IP-INF*)
   AND ({1}NP-OB* idoms \*T\**)
   AND (NP* sameIndex \*T\**)

add_leaf_before{1}: (CODE *ZZZ_WRONG_TRACE*)
