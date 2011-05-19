node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms [1]{1}finiteVerb)
   AND (IP* iDoms [2]{2}finiteVerb)

add_leaf_before{1}: (CODE *ZZZ_2FINITE*)
append_label{2}: -ZZZ-2FINITE