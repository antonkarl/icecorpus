node: CP*

copy_corpus: t

query: (CP* iDoms W*)
   AND (CP* doms {1}\*ICH\**)
   AND (W* sameIndex \*ICH\**)

append_label{1}: -ZZZ-WRONG_TRACE
