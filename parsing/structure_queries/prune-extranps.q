copy_corpus:t

node: IP*
query: ([1]NP* idoms [2]{1}NP) AND ([1]NP* idoms [3]{2}NP) AND ([1]NP* idoms CONJ) AND ([2]NP idomstotal 1) AND ([3]NP idomstotal 1)

delete_node{1}:
delete_node{2}: