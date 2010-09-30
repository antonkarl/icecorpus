node: IP*
define: def/ICE.def

copy_corpus: t

query: ({1}NP-VOC idoms *-A|*-D|*-G)

append_label{1}: -ZZZ-BAD-NP-VOC
