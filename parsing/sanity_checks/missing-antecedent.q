node: CP*

copy_corpus: t

query: ({1}CP* iDoms !W*)
   AND (CP* iDoms IP*)
   AND (IP* iDomsMod ADJP*|ADVP*|NP*|PP* \*T\**)

add_leaf_before{1}: (CODE *ZZZ_MISS_ANTECEDENT*)
