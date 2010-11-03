copy_corpus:t

define: def/verbtopic.def
node: IP*
query: 
([1]IP* idoms {2}IP-SUB) AND ({1}CP* iprecedes IP-SUB) AND (CP* idoms ![2]IP*)

extend_span{1, 2}: