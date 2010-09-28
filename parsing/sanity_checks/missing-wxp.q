node: IP*|FRAG

copy_corpus: t

define: def/ICE.def

query: ({1}CP-REL*|CP-CMP* exists) AND (CP-REL*|CP-CMP* idoms !\**) AND (CP-REL*|CP-CMP* idoms !W*P*)

append_label{1}: -ZZZ-MISS-WXP