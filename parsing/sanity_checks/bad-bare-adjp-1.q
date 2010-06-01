node: IP*

copy_corpus: t

define: def/ICE.def

query: (IP* iDoms {1}ADJP)
   AND (IP* iDoms finiteVerb)
   AND (IP* iDoms !B*)
   AND (IP* iDomsMod V*|M*|R* !linkingVerb)

append_label{1}: -ZZZ-BARE_ADJP