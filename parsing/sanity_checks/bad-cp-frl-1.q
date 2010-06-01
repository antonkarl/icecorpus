node: IP*|FRAG*

copy_corpus: t

query: (!ADJP-SPR|ADVP*|NP*|CP-FRL*|CONJP idoms {1}CP-FRL*)

append_label{1}: -ZZZ-NEEDS_DOMINATION