copy_corpus:t

node: IP*
query: (IP* idoms {1}ADJP*) AND (ADJP* idoms {2}ADV) AND (ADV idoms [Ss]vo*) AND (ADJP* idoms {3}ADJ*) AND (ADJ* idomsonly segjandi*|mælandi*)

replace_label{1}: IP-PPL
add_internal_node{2, 2}: ADVP
replace_label{3}: VAG