node: IP*

copy_corpus: t

query: (IP-INF* iDoms NP-OB*)
   AND (IP* idoms IP-INF*)
   AND (NP-OB* idoms {1}\*T\**)
   AND (NP* sameIndex \*T\**)

append_label{1}: -ZZZ-WRONG_TRACE
