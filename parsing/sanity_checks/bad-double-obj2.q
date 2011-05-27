node: IP*

copy_corpus: t

query: (IP* iDoms [1]NP-OB2)
   AND (IP* iDoms [2]{1}NP-OB2)

add_leaf_before{1}: (CODE *ZZZ_BAD_DOUBLE_OBJECTS*)