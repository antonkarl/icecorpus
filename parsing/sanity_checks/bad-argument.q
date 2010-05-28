node: $ROOT

copy_corpus: t

query: (!IP* iDoms {1}*-SBJ*|*-OB[12]*)

append_label{1}: -ZZZ-BAD-ARG
