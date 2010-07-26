copy_corpus:t

define: def/verbtopic.def
node: $ROOT
query: 
({1}IP-SUB hassister [1]*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*) AND (IP-SUB precedes {2}[1]*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

extend_span{1, 2}: