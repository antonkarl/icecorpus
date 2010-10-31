copy_corpus:t

define: def/verbtopic.def
node: $ROOT
query: 
(CP* idoms {1}IP-SUB) AND (CP* hassister [1]{2}*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*) AND (IP-SUB precedes {2}[1]*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

extend_span{1, 2}: