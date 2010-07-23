copy_corpus:t

node:IP*
query: (IP* idoms {1}NP*) AND (NP* idoms {2}N*) AND (N* idomsonly [Ee]m-[Ee]m)

delete_node{1}:
replace_label{2}: BEPI