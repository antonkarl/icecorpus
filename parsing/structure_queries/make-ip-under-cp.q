copy_corpus:t

node: IP*
query: (CP* idoms !IP-SUB) AND (CP* idomsnumber 2 {1}N*P*|A*P*|PP*|NEG)

add_internal_node{1, 1}: IP-SUB
