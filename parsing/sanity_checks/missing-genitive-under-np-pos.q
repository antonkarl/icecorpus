node: $ROOT

copy_corpus: t

query: (NP-POS* iDoms {1}N*-N|N*-A|N*-D)

append_label{1}: -ZZZ-MISS_GENITIVE
