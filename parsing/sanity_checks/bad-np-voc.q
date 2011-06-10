node: IP*
define: def/ICE.def

copy_corpus: t

query: ({1}NP-VOC idoms *-A|*-D|*-G)

add_leaf_before{1}: (CODE *ZZZ_BAD_NP_VOC*)
