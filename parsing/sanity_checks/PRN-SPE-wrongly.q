node: $ROOT

copy_corpus: t

query: ({1}*PRN*SPE*|*SBJ*SPE* exists)

append_label{1}: -ZZZ-SPE-PRN-OR-SPE-SBJ
