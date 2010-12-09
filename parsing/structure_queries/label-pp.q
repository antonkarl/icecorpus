copy_corpus:t

node: IP*
query: ({1}ADVP idoms {2}ADV) AND (ADV idoms í-*|á-*|til-*|af-*|með-*|frá-*|við-*|fyrir-*|úr-*|*vegna-*)

replace_label{1}: PP
replace_label{2}: P