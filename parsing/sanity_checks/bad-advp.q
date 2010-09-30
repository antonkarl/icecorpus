node: $ROOT

copy_corpus: t

query: ({1}ADVP* idoms ADV) AND (ADVP* idoms RP)

append_label{1}: -ZZZ-BAD-ADVP-PROBABLY-PP
