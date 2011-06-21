node: CP*

copy_corpus: t

query: (CP* iDoms W*)
   AND ({1}CP* doms \*ICH\**)
   AND (W* sameIndex \*ICH\**)

add_leaf_before{1}: (CODE *ZZZ_WRONG_TRACE*)
