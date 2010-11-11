copy_corpus:t

node: IP*
query: ({1}ADVP|PP idoms {2}ADV|P) AND (ADV|P idoms út-*|upp-*|inn-*|niður-*)

delete_node{1}:
replace_label{2}: P