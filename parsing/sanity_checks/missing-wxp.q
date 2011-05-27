node: IP*|FRAG|QTP

copy_corpus: t

define: def/ICE.def

query: ([1]{1}CP-REL*|CP-CMP* exists) AND ([1]CP-REL*|CP-CMP* idoms !\**) AND ([1]CP-REL*|CP-CMP* idoms !W*P*) AND ([1]CP-REL*|CP-CMP* idoms ![2]CP-REL*|CP-CMP*)

add_leaf_before{1}: (CODE *ZZZ_MISS_WXP*)