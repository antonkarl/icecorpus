copy_corpus:t

node: IP*
query: 
({1}CP* idoms !IP-SUB) AND (CP* idoms !N*P*|A*P*|PP*|NEG) AND (CP* iprecedes {2}N*P*|A*P*|PP*|NEG)

extend_span{1, 2}: