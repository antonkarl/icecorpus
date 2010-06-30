node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}CP-ADV* exists) AND (

append_label{1}: -ZZZ-PRN
