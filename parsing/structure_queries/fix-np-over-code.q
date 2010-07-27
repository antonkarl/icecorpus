copy_corpus:t
ignore_nodes: COMMENT|ID|LB|'|\"|,|E_S|.|/|RMV:*

node:IP*
query: ({1}NP* idomsonly CODE)


delete_node{1}:
