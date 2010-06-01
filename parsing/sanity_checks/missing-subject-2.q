node: IP*

define: def/ICE.def

copy_corpus: t

query: ({1}IP-MAT*|IP-SUB*|IP-SMC* iDoms finiteVerb)
   AND (IP-MAT*|IP-SUB*|IP-SMC* iDoms !*-SBJ*)
   AND (IP-MAT*|IP-SUB*|IP-SMC* iDoms !CONJP)

append_label{1}: -ZZZ-MISS_SBJ
