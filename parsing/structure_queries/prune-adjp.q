copy_corpus:t

node: IP*
query: ([1]{1}ADJP* idomsonly ADJ-*|ADJS-*|ADJR-*|Q-*|QS-*|QR-*) AND (NP*|ADVP*|[2]ADJP* idoms [1]ADJP*)

delete_node{1}:
