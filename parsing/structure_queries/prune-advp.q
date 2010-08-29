copy_corpus:t

node: IP*
query: ([1]ADVP* exists) AND ([1]{1}ADVP* idomsonly ADV) AND (NP*|ADJP*|[2]ADVP idoms [1]ADVP*)

delete_node{1}:
