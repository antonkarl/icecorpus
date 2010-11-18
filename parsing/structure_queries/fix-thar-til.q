copy_corpus:t

node: IP*
query: ({1}CP* idoms [1]ADV) AND (CP* idoms [2]{2}ADV) AND ([1]ADV idoms þar-*) AND ([2]ADV idoms til-*) AND (CP* idoms {3}BEPI|C) AND (BEPI|C idoms er-*)

replace_label{1}: PP
replace_label{2}: P
add_internal_node{3, 3}: CP-ADV
replace_label{3}: C