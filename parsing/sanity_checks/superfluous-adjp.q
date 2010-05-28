node: NP*|WNP*

copy_corpus: t

define: def/ICE.def

query: ({1}ADJP|QP iDomsOnly ADJ-*|ADJR-*|ADJS-*|VA*|Q*)
   AND (ADJP|QP precedes noun)
   AND (ADJP|QP hasSister noun)

append_label{1}: -ZZZ
