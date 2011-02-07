copy_corpus:t

node: IP*
query: ({1}CP idoms ADV) AND (CP idoms {2}C) AND (ADV idoms áður|áður-áður) AND (ADV iprecedes C) AND (C idoms en|en-en)

replace_label{1}: ADVP-TMP
replace_label{2}: P
add_internal_node{2, 2}: PP
add_leaf_after{2}: (C 0)
add_leaf_after{2}: (WADVP 0)
