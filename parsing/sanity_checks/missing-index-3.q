node: $ROOT

copy_corpus: t

query: ({1}\*ICH\*|\*T\* exists)

append_label{1}: -ZZZ-MISS_INDEX
