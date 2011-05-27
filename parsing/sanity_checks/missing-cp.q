node: $ROOT

copy_corpus: t

query: (!{1}CP*|CONJP|IP-SUB* iDoms IP-SUB*)

add_leaf_before{1}: (CODE *ZZZ_MISS_CP*)
