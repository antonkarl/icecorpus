copy_corpus:t

node: IP*
query: ([1]NP* idoms [2]NP) AND ([1]NP* idoms [3]{1}NP) AND ([1]NP* idoms {2}CONJ) AND (CONJ iprecedes [3]NP) AND ([2]NP idomstotal> 1) AND ([3]NP idomstotal> 1)

add_internal_node{2, 1}: CONJP