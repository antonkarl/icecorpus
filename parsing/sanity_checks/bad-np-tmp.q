node: IP*
define: def/ICE.def

copy_corpus: t

query: ({1}NP-TMP* idoms *-N)

append_label{1}: -ZZZ-BAD-CASE
