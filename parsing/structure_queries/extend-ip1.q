copy_corpus:t

define: def/verbtopic.def
node: IP*
query: 
({1}IP-SUB hassister {2}*VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N) AND (IP-SUB precedes *VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N)

extend_span{1, 2}: