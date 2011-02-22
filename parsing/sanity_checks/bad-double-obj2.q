node: IP*

copy_corpus: t

query: (IP* iDoms [1]NP-OB2)
   AND (IP* iDoms [2]{1}NP-OB2)

append_label{1}: -ZZZ-BAD-DOUBLE-OBJECTS