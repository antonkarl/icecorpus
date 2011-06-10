node: IP*|CP*

copy_corpus: t

query: ((CP* idoms {1}IP-MAT|IP-MAT-SPE*|IP-MAT=*|IP-MAT-1*) AND (CP* idoms *C*))
OR
(CP*MISS_C* idoms IP-MAT|IP-MAT-SPE*|IP-MAT=*|IP-MAT-1*)

add_leaf_before{1}: (CODE *ZZZ_SUB*)