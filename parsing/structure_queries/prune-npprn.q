copy_corpus:t

node: IP*
query: (IP* idoms [1]NP*) AND ([1]NP* idoms [2]{1}NP) AND ([1]NP* idoms [3]{2}NP) AND ([1]NP* idoms !CONJ*) AND ([2]NP precedes [3]NP)

delete_node{1}:
append_label{2}: -PRN