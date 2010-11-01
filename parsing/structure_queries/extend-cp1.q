copy_corpus:t

define: def/verbtopic.def
node: IP*
query: 
({1}CP* hassister [1]{2}*VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N) AND (CP* precedes [1]*VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N)

extend_span{1, 2}: