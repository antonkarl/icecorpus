node: IP*|CP*

copy_corpus: t

query: ((CP* idoms {1}IP-MAT*) AND (CP* idoms *C*))
OR
(CP*MISS_C* idoms IP-MAT*)

append_label{1}: -ZZZ-SUB