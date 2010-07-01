node: $ROOT

copy_corpus: t

query: 
($ROOT doms {1}\*T\**)
   AND (!W*P* sameIndex \*T\**)

append_label{1}: -ZZZ-WRONG_TRACE
