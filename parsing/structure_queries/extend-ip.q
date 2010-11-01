copy_corpus:t

define: def/verbtopic.def
node: IP*
query: 
({1}IP-SUB hassister {2}*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*) AND (IP-SUB precedes *MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

extend_span{1, 2}: