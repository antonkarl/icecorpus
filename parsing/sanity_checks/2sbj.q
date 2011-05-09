node: $ROOT|IP*

copy_corpus: t

query: (IP*|RRC* iDoms [1]{1}*SBJ*)
   AND (IP*|RRC* iDoms [2]*SBJ*)

append_label{1}: -ZZZ-TWOSBJ
