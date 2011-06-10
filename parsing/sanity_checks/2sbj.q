node: $ROOT|IP*

copy_corpus: t

query: (IP*|RRC* iDoms [1]{1}*SBJ*)
   AND (IP*|RRC* iDoms [2]*SBJ*)

add_leaf_before{1}: (CODE *ZZZ_TWOSBJ*)
