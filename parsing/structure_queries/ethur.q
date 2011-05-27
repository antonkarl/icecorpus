copy_corpus:t

node: IP*
query: ({1}CP* idoms {2}C) AND (C idoms eður*|Eður*|hvor*ki*|Hvor*ki*)

delete_node{1}:
replace_label{2}: CONJ