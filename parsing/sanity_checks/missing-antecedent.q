node: CP*

copy_corpus: t

query: ({1}CP* iDoms !W*)
   AND (CP* iDoms IP*)
   AND (IP* iDomsMod ADJP*|ADVP*|NP*|PP* \*T\**)

append_label{1}: -ZZZ
