node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms {1}[1]VB|DO|RD|BE|HV)
   AND (IP* iDoms [2]VB|DO|RD|BE|HV)

append_label{1}: -ZZZ-NO-IP-INF