node: IP*

copy_corpus: t

query: ({1}IP-SUB*|IP-MAT*|IP-IMP* iDoms *-RSP)
   AND (IP-SUB*|IP-MAT*|IP-IMP* iDoms !*-LFD|*-LFD-SPE)

add_leaf_before{1}: (CODE *ZZZ_MISS_LFD*)
