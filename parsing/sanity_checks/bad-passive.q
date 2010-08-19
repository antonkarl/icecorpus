copy_corpus: t
define: def/ICE.def

node: IP*|CP*|FRAG 	
query: (nongap_ip idoms {1}*AN) AND (nongap_ip idoms !BE*|RD*)

append_label{1}: -ZZZ-BAD-VAN-MAYBE-VBN
