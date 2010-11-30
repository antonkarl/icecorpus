node: IP*SPE*|CP*SPE*|QTP

define: def/ICE.def

copy_corpus: t

query: (IP*SPE*|CP*SPE*|QTP doms {1}nonspe_ip)
AND
(!IP-MAT-PRN doms nonspe_ip)

append_label{1}: -ZZZ-MISS-SPE
