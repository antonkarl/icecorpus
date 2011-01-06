node: $ROOT

copy_corpus: t

query: ({1}VB* hasSister VB*|VAN)

append_label{1}: -ZZZ-PROBABLY_NOT_VB
