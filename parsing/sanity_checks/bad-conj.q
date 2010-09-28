define: def/ICE.def

node: IP*|FRAG

copy_corpus: t

query: ([1]nongap_ip idoms {1}CONJ) AND ([2].* ISROOT)

append_label{1}: -ZZZ-BAD-CONJ
