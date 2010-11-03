copy_corpus:t

node: IP*
query: (CP* idoms !IP-SUB) AND (CP* idoms {1}N*P*|A*P*|PP*)

add_internal_node{1, 1}: IP-SUB
