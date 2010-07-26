copy_corpus:t

define: ../def/verbtopic.def
node: $ROOT
query: 
({1}IP-SUB hassister [1]*VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N) AND (IP-SUB precedes {2}[1]*VB|V*N*|*HV|H*N*|*DO|D*N*|*BE|B*N*|*AX|AXN*|*RD|R*N)

extend_span{1, 2}: