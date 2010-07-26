copy_corpus:t

node: IP*
query: (ADVP* exists) AND (ADVP* idoms [1]ADV) AND (ADVP* idoms {1}[2]ADV|NEG) AND ([2]ADV|NEG idoms *ekki*|*eigi*)

move_up_node{1}:
