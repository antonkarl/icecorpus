copy_corpus:t

node: IP*
query: (ADVP idoms {1}ADV*) AND (ADV* idomsonly svo*) AND (ADVP idoms {2}C) AND (C idomsonly sem*)

replace_label{1}: ADVR
add_internal_node{2, 2}: CP-CMP