node: PP*

copy_corpus: t

query: (PP* iDoms !{1}\**|P|*+P|ADJP|ADVP|CP-*|FRAG|IP-*|INTJP|NEG|NP|NUMP|PP|QTP)
//   AND (PP* iDoms !NP-RSP)

append_label{1}: -ZZZ-BAD_PP_COMPL
