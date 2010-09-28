node: IP*|FRAG

copy_corpus: t

define: def/ICE.def

query: ([1]{1}CP-REL*|CP-CMP* exists) AND ([1]CP-REL*|CP-CMP* idoms !\**) AND ([1]CP-REL*|CP-CMP* idoms !W*P*) AND ([1]CP-REL*|CP-CMP* idoms ![2][1]CP-REL*|CP-CMP*)

append_label{1}: -ZZZ-MISS-WXP