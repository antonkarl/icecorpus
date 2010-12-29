copy_corpus:t

node:IP*
query: (IP* idoms {1}CP*) AND (CP* idomsonly {2}C) AND (C idomsonly þá-*|Þá-*)

replace_label{1}: ADVP-TMP
replace_label{2}: ADV