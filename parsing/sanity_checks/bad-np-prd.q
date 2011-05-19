node: IP*
define: def/ICE.def

copy_corpus: t

query: (IP-MAT*|IP-SUB* idoms finiteVerb)
       AND (IP-MAT*|IP-SUB* idoms {1}NP-PRD)
       AND (NP-PRD idoms *-A|*-D|*-G)

add_leaf_before{1}: (CODE *ZZZ_BAD_NP_PRD*)
