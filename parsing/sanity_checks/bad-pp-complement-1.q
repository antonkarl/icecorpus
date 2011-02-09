node: PP*

copy_corpus: t

query: (PP* iDoms P) AND (PP* idoms !{1}\**|*+P|ADJP|ADVP|CP-*|NEG|NP|PP) AND (PP idomstotal> 1)

append_label{1}: -ZZZ-BAD_PP_COMPL
