node: IP*
define: def/ICE.def

copy_corpus: t

query: ({1}NP-TMP* idoms *-N)

add_leaf_before{1}: (CODE *ZZZ_BAD_CASE*)
