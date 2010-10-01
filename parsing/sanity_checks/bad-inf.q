node: IP*

define: def/ICE.def

copy_corpus: t

query: (IP* iDoms [1]VB|DO|RD|BE|VBP*|DOP*|RDP*|BEP*|VBD*|DOD*|RDD*|BED*)
   AND (IP* iDoms [2]{1}VB|DO|RD|BE|RD|MD)

append_label{1}: -ZZZ-NO-IP-INF