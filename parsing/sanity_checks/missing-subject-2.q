node: IP*

define: def/ICE.def

copy_corpus: t

query: ({1}IP* iDoms finiteVerb)
   AND (IP* iDoms !*-SBJ*)
   AND (IP* iDoms !CONJP)

append_label{1}: -ZZZ
