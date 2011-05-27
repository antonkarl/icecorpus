node: IP*
define: def/ICE.def

copy_corpus: t

query: (P hasSister NP)
AND ({1}NP idoms *-N)
AND (P idoms !of|en*|nema*)

add_leaf_before{1}: (CODE *ZZZ_BAD_PP_CASE*)
