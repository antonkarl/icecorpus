copy_corpus:t

define: def/verbtopic.def
node: $ROOT
query: 
({1}CP* hassister {2}*MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*) AND (CP* precedes *MD*|*HVP*|*HVD*|*DOP*|*DOD*|*BEP*|*BED*|*VBP|*VBD*|*AXD*|*AXP*|*RDP*|*RDD*)

extend_span{1, 2}: