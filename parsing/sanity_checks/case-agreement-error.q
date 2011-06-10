node: NP*
//define: def/ICE.def

copy_corpus: t

query:       (({1}NP*|NX idomsmod NP-PRN *-N)
             AND ( (NP*|NX idomsmod NP-PRN *-A) OR (NP*|NX idomsmod NP-PRN *-D) OR (NP*|NX idomsmod NP-PRN *-G) ))
       OR ( (NP*|NX idomsmod NP-PRN *-A) 
             AND ( (NP*|NX idomsmod NP-PRN *-D) OR (NP*|NX idomsmod NP-PRN *-G) ) )
       OR ( (NP*|NX idomsmod NP-PRN *-D) 
             AND ( (NP*|NX idomsmod NP-PRN *-G) ) )
       
add_leaf_before{1}: (CODE *ZZZ_CASE_AGREEMENT_ERROR*)
