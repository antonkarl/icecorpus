node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms [1]finiteVerb|VB|DO|RD|BE|RD|MD)
   AND (IP* iDoms [2]{1}VB|DO|RD|BE|RD|MD)

append_label{1}: -ZZZ-NO-IP-INF