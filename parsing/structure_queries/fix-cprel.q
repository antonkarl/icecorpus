copy_corpus:t

node: IP*
query: (IP* idoms {1}CP-REL) AND (CP-REL iprecedes {2}.*) AND (CP-REL hassister .*)  

extend_span{1, 2}:
add_internal_node{2, 2}: IP-SUB
