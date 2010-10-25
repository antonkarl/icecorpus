node: NP*
define: def/ICE.def

copy_corpus: t

query:       (({1}NP*|NX idoms *-N)
             AND ( (NP*|NX idoms *-A) OR (NP*|NX idoms *-D) OR (NP*|NX idoms *-G) ))
       OR ( (NP*|NX idoms *-A) 
             AND ( (NP*|NX idoms *-D) OR (NP*|NX idoms *-G) ) )
       OR ( (NP*|NX idoms *-D) 
             AND ( (NP*|NX idoms *-G) ) )
       
append_label{1}: -ZZZ-CASE-AGREEMENT-ERROR
