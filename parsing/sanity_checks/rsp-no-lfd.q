node: IP*

copy_corpus: t

query: ({1}IP* iDoms *-RSP)
   AND (IP* iDoms !*-LFD|*-LFD-SPE)

append_label{1}: -ZZZ-MISS_LFD
