node: $ROOT

copy_corpus: t

query: (IP* idoms [1]VB*|VAN) AND ({1}[1]VB*|VAN hasSister [2]VB*|VAN)
       AND ([1]VB*|VAN hasSister !CONJ)

append_label{1}: -ZZZ-PROBABLY_NOT_VB
