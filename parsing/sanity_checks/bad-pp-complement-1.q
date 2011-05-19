node: PP*

copy_corpus: t

query: (PP* iDoms P) AND (PP* idoms !{1}\**|*+P|ADJP|ADVP|ADVP-RSP*|CP-*|NEG|NP|PP|IP-INF*|IP-SMC*|IP-PPL*) AND (PP idomstotal> 1)

add_leaf_before{1}: (CODE *ZZZ_BAD_PP_COMPL*)
