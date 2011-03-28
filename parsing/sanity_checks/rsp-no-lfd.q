node: IP*

copy_corpus: t

query: ({1}IP-SUB*|IP-MAT*|IP-IMP* iDoms *-RSP)
   AND (IP-SUB*|IP-MAT*|IP-IMP* iDoms !*-LFD|*-LFD-SPE)

append_label{1}: -ZZZ-MISS_LFD
