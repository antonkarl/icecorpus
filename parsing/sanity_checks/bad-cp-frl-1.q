node: IP*|FRAG*|QTP

copy_corpus: t

query: (!ADJP-SPR|ADVP*|NP*|CP-FRL*|CONJP idoms {1}CP-FRL*)

add_leaf_before{1}: (CODE *ZZZ_NEEDS_DOMINATION*)