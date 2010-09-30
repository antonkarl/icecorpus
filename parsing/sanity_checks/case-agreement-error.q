node: NP*
define: def/ICE.def

copy_corpus: t

query:       (({1}NP* idoms *-N)
             AND ( (NP* idoms *-A) OR (NP* idoms *-D) OR (NP* idoms *-G) ))
       OR ( (NP* idoms *-A) 
             AND ( (NP* idoms *-D) OR (NP* idoms *-G) ) )
       OR ( (NP* idoms *-D) 
             AND ( (NP* idoms *-G) ) )
       
append_label{1}: -ZZZ-CASE-AGREEMENT-ERROR
