node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms {1}[1]VB|DO|RD|BE|HV|MD)
   AND (IP* iDoms [2]VB|DO|RD|BE|HV|MD)

append_label{1}: -ZZZ-NO-IP-INF