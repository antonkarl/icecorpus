node: $ROOT

copy_corpus: t

query: (!{1}CP*|CONJP|IP-SUB* iDoms IP-SUB*)

append_label{1}: -ZZZ
